# EMA Hourly Continuation — SKL/USDT P34_50

**Symbol:** SKL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.5802 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.8099 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -3.0509 |
| sortino_ratio | -0.7464 |
| max_drawdown | 0.5951 |
| cagr | -0.2907 |
| net_avg_win | 61.4594 |
| net_avg_loss | -83.9602 |
| avg_hold_time_bars | 5.5680 |
| exposure | 0.0744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
