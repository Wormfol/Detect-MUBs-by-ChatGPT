import { FC, SVGProps } from 'react'

const DexterityCapital: FC<SVGProps<SVGSVGElement>> = ({ id, ...props }) => (
  <svg
    width="189"
    height="189"
    viewBox="0 0 189 189"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    xmlnsXlink="http://www.w3.org/1999/xlink"
    {...props}
  >
    <circle cx="94.0704" cy="94.0704" r="94.0704" fill="black" />
    <rect x="31" y="31" width="126" height="126" fill={`url(#${id})`} />
    <defs>
      <pattern
        id={id}
        patternContentUnits="objectBoundingBox"
        width="1"
        height="1"
        className="animate-maintain-svg"
      >
        <use xlinkHref="#image0_103_74" transform="scale(0.00195312)" />
      </pattern>
      <image
        id="image0_103_74"
        width="512"
        height="512"
        xlinkHref="data:image/png;base64,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AgQIBBYQAAI3R2kECBAgQCCVgACQSta6BAgQIEAgsIAAELg5SiNAgAABAqkEBIBUstYlQIAAAQKBBQSAwM1RGgECBAgQSCUgAKSStS4BAgQIEAgsIAAEbo7SCBAgQIBAKgEBIJWsdQkQIECAQGABASBwc5RGgAABAgRSCQgAqWStS4AAAQIEAgsIAIGbozQCBAgQIJBKQABIJWtdAgQIECAQWEAACNwcpREgQIAAgVQCAkAqWesSIECAAIHAAgJA4OYojQABAgQIpBIQAFLJWpcAAQIECAQWEAACN0dpBAgQIEAglYAAkErWugQIECBAILCAABC4OUojQIAAAQKpBASAVLLWJUCAAAECgQUEgMDNURoBAgQIEEglIACkkrUuAQIECBAILCAABG6O0ggQIECAQCoBASCVrHUJECBAgEBgAQEgcHOURoAAAQIEUgkIAKlkrUuAAAECBAILCACBm6M0AgQIECCQSkAASCVrXQIECBAgEFhAAAjcHKURIECAAIFUAgJAKlnrEiBAgACBwAICQODmKI0AAQIECKQSEABSyVqXAAECBAgEFhAAAjdHaQQIECBAIJWAAJBK1roECBAgQCCwgAAQuDlKI0CAAAECqQQEgFSy1iVAgAABAoEFBIDAzVEaAQIECBBIJSAApJK1LgECBAgQCCwgAARujtIIECBAgEAqAQEglax1CRAgQIBAYAEBIHBzlEaAAAECBFIJCACpZK1LgAABAgQCCwgAgZujNAIECBAgkEpAAEgla10CBAgQIBBYQAAI3BylESBAgACBVAICQCpZ6xIgQIAAgcACAkDg5iiNAAECBAikEhAAUslalwABAgQIBBYQAAI3R2kECBAgQCCVgACQSta6BAgQIEAgsIAAELg5SiNAgAABAqkEBIBUstYlQIAAAQKBBQSAwM1RGgECBAgQSCUgAKSStS4BAgQIEAgsIAAEbo7SCBAgQIBAKgEBIJWsdQkQIECAQGABASBwc5RGgAABAgRSCQgAqWStS4AAAQIEAgsIAIGbozQCBAgQIJBKQABIJWtdAgQIECAQWEAACNwcpREgQIAAgVQCAkAqWesSIECAAIHAAgJA4OYojQABAgQIpBIQAFLJWpcAAQIECAQWEAACN0dpBAgQIEAglYAAkErWugQIECBAILCAABC4OUojQIAAAQKpBASAVLLWJUCAAAEC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"
      />
    </defs>
  </svg>
)

export default DexterityCapital
