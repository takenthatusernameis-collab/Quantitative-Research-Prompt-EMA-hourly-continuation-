# EMA Hourly Continuation — LUNC/USDT P100_144

**Symbol:** LUNC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.7282 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0177 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.4416 |
| sortino_ratio | -0.3083 |
| max_drawdown | 0.3229 |
| cagr | -0.1316 |
| net_avg_win | 71.3679 |
| net_avg_loss | -100.7073 |
| avg_hold_time_bars | 7.9050 |
| exposure | 0.0794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
