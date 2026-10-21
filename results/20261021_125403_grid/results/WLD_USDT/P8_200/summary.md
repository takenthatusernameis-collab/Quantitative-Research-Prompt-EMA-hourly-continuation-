# EMA Hourly Continuation — WLD/USDT P8_200

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.9575 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0622 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -0.1690 |
| sortino_ratio | -0.0370 |
| max_drawdown | 0.1596 |
| cagr | -0.0207 |
| net_avg_win | 96.0092 |
| net_avg_loss | -107.4293 |
| avg_hold_time_bars | 77.6121 |
| exposure | 0.8185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
