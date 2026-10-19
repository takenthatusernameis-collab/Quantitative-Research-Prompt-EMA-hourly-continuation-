# EMA Hourly Continuation — JASMY/USDT P55_100

**Symbol:** JASMY/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.5379 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8890 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -4.6948 |
| sortino_ratio | -1.6587 |
| max_drawdown | 0.8788 |
| cagr | -0.5576 |
| net_avg_win | 33.2487 |
| net_avg_loss | -56.6100 |
| avg_hold_time_bars | 5.0909 |
| exposure | 0.1476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
