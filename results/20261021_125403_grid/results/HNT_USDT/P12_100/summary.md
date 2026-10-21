# EMA Hourly Continuation — HNT/USDT P12_100

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7847 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9364 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.5249 |
| sortino_ratio | -0.4841 |
| max_drawdown | 0.4448 |
| cagr | -0.2015 |
| net_avg_win | 64.7415 |
| net_avg_loss | -79.5586 |
| avg_hold_time_bars | 23.5535 |
| exposure | 0.5300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
