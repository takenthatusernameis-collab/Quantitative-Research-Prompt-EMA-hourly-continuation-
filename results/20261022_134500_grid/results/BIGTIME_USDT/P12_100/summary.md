# EMA Hourly Continuation — BIGTIME/USDT P12_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.8043 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.1186 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -1.6859 |
| sortino_ratio | -0.5862 |
| max_drawdown | 0.5290 |
| cagr | -0.2414 |
| net_avg_win | 65.9162 |
| net_avg_loss | -89.6877 |
| avg_hold_time_bars | 21.5376 |
| exposure | 0.5838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
