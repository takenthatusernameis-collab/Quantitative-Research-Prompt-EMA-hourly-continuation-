# EMA Hourly Continuation — LSK/USDT P100_144

**Symbol:** LSK/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.5058 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -4.4367 |
| sortino_ratio | -1.3187 |
| max_drawdown | 0.8119 |
| cagr | -0.4709 |
| net_avg_win | 40.6320 |
| net_avg_loss | -67.2727 |
| avg_hold_time_bars | 6.5601 |
| exposure | 0.1315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
