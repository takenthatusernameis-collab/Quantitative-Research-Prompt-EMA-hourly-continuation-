# EMA Hourly Continuation — IMX/USDT P20_200

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 1.1008 |
| net_win_rate | 0.5617 |
| gross_profit_factor | 1.2884 |
| gross_win_rate | 0.5617 |
| sharpe_ratio | 0.5429 |
| sortino_ratio | 0.1387 |
| max_drawdown | 0.1253 |
| cagr | 0.0551 |
| net_avg_win | 91.5446 |
| net_avg_loss | -106.5720 |
| avg_hold_time_bars | 46.3539 |
| exposure | 0.6460 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
