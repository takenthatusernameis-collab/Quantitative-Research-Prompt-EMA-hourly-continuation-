# EMA Hourly Continuation — TRB/USDT P34_100

**Symbol:** TRB/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.6530 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8460 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -2.6226 |
| sortino_ratio | -0.7580 |
| max_drawdown | 0.5911 |
| cagr | -0.2935 |
| net_avg_win | 57.2171 |
| net_avg_loss | -75.7784 |
| avg_hold_time_bars | 14.2246 |
| exposure | 0.2665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
