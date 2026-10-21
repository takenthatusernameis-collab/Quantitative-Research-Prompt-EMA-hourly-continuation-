# EMA Hourly Continuation — IMX/USDT P26_50

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8402 |
| net_win_rate | 0.5306 |
| gross_profit_factor | 1.1173 |
| gross_win_rate | 0.5306 |
| sharpe_ratio | -1.0563 |
| sortino_ratio | -0.3198 |
| max_drawdown | 0.3249 |
| cagr | -0.1379 |
| net_avg_win | 70.1507 |
| net_avg_loss | -94.3815 |
| avg_hold_time_bars | 5.6848 |
| exposure | 0.1134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
