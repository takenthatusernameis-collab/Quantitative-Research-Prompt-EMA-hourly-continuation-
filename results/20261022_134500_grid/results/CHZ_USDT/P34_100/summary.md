# EMA Hourly Continuation — CHZ/USDT P34_100

**Symbol:** CHZ/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.5246 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.9128 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -4.5982 |
| sortino_ratio | -1.5843 |
| max_drawdown | 0.8585 |
| cagr | -0.5364 |
| net_avg_win | 33.3411 |
| net_avg_loss | -56.5561 |
| avg_hold_time_bars | 10.9567 |
| exposure | 0.2993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
