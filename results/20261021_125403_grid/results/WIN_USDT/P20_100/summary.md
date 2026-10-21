# EMA Hourly Continuation — WIN/USDT P20_100

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7123 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 0.9714 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -2.0222 |
| sortino_ratio | -0.5863 |
| max_drawdown | 0.5648 |
| cagr | -0.2369 |
| net_avg_win | 59.8029 |
| net_avg_loss | -83.1442 |
| avg_hold_time_bars | 22.1244 |
| exposure | 0.4123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
