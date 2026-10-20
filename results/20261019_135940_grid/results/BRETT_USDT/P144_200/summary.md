# EMA Hourly Continuation — BRETT/USDT P144_200

**Symbol:** BRETT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6122 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -3.2484 |
| sortino_ratio | -0.8984 |
| max_drawdown | 0.6679 |
| cagr | -0.3479 |
| net_avg_win | 58.8418 |
| net_avg_loss | -86.5026 |
| avg_hold_time_bars | 4.4543 |
| exposure | 0.0774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
