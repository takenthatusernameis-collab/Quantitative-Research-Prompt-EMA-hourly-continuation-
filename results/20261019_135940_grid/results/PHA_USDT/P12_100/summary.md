# EMA Hourly Continuation — PHA/USDT P12_100

**Symbol:** PHA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.6514 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9355 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -3.5110 |
| sortino_ratio | -1.2528 |
| max_drawdown | 0.8010 |
| cagr | -0.4564 |
| net_avg_win | 47.0907 |
| net_avg_loss | -65.5423 |
| avg_hold_time_bars | 19.3425 |
| exposure | 0.5750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
