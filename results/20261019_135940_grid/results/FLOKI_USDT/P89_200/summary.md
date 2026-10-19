# EMA Hourly Continuation — FLOKI/USDT P89_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5603 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8498 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -3.2446 |
| sortino_ratio | -0.8497 |
| max_drawdown | 0.6431 |
| cagr | -0.3343 |
| net_avg_win | 51.3001 |
| net_avg_loss | -78.2668 |
| avg_hold_time_bars | 14.0899 |
| exposure | 0.2210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
