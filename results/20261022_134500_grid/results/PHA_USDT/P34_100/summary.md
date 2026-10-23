# EMA Hourly Continuation — PHA/USDT P34_100

**Symbol:** PHA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.5082 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.7563 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -5.0308 |
| sortino_ratio | -1.8433 |
| max_drawdown | 0.8921 |
| cagr | -0.5834 |
| net_avg_win | 31.2462 |
| net_avg_loss | -46.8319 |
| avg_hold_time_bars | 7.9191 |
| exposure | 0.2448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
