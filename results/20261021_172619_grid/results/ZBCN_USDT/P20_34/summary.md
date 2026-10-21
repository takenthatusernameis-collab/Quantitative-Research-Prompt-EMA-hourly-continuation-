# EMA Hourly Continuation — ZBCN/USDT P20_34

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 1.0468 |
| net_win_rate | 0.5708 |
| gross_profit_factor | 1.3149 |
| gross_win_rate | 0.5708 |
| sharpe_ratio | 0.2709 |
| sortino_ratio | 0.0601 |
| max_drawdown | 0.1427 |
| cagr | 0.0215 |
| net_avg_win | 93.3990 |
| net_avg_loss | -118.6572 |
| avg_hold_time_bars | 5.8982 |
| exposure | 0.0617 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
