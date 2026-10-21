# EMA Hourly Continuation — ATOM/USDT P12_26

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.6297 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9255 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.9089 |
| sortino_ratio | -0.8456 |
| max_drawdown | 0.6227 |
| cagr | -0.3191 |
| net_avg_win | 53.4468 |
| net_avg_loss | -78.4973 |
| avg_hold_time_bars | 5.6195 |
| exposure | 0.1047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
