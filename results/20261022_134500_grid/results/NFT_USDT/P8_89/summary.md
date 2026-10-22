# EMA Hourly Continuation — NFT/USDT P8_89

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1330 |
| net_profit_factor | 0.2976 |
| net_win_rate | 0.2639 |
| gross_profit_factor | 0.7525 |
| gross_win_rate | 0.3030 |
| sharpe_ratio | -18.9074 |
| sortino_ratio | -10.2924 |
| max_drawdown | 1.0000 |
| cagr | -0.9964 |
| net_avg_win | 12.0699 |
| net_avg_loss | -14.5419 |
| avg_hold_time_bars | 9.3008 |
| exposure | 0.5623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
