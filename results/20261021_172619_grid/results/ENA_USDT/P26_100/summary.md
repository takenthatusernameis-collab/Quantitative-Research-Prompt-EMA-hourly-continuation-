# EMA Hourly Continuation — ENA/USDT P26_100

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.9316 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0850 |
| gross_win_rate | 0.5239 |
| sharpe_ratio | -0.4196 |
| sortino_ratio | -0.1266 |
| max_drawdown | 0.3139 |
| cagr | -0.0621 |
| net_avg_win | 88.3554 |
| net_avg_loss | -103.4289 |
| avg_hold_time_bars | 16.4624 |
| exposure | 0.3285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
