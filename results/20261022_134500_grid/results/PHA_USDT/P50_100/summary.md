# EMA Hourly Continuation — PHA/USDT P50_100

**Symbol:** PHA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.4862 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.7590 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -5.7214 |
| sortino_ratio | -2.0319 |
| max_drawdown | 0.9180 |
| cagr | -0.6258 |
| net_avg_win | 31.9559 |
| net_avg_loss | -48.1426 |
| avg_hold_time_bars | 5.8768 |
| exposure | 0.1712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
