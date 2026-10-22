# EMA Hourly Continuation — PUFFER/USDT P20_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 1.1884 |
| net_win_rate | 0.5720 |
| gross_profit_factor | 1.3433 |
| gross_win_rate | 0.5720 |
| sharpe_ratio | 0.9480 |
| sortino_ratio | 0.2417 |
| max_drawdown | 0.0974 |
| cagr | 0.1026 |
| net_avg_win | 98.8086 |
| net_avg_loss | -111.1281 |
| avg_hold_time_bars | 45.1070 |
| exposure | 0.6203 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
