# EMA Hourly Continuation — KCS/USDT P21_34

**Symbol:** KCS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.2931 |
| net_win_rate | 0.3621 |
| gross_profit_factor | 0.6435 |
| gross_win_rate | 0.3759 |
| sharpe_ratio | -6.2058 |
| sortino_ratio | -1.5490 |
| max_drawdown | 0.8425 |
| cagr | -0.5210 |
| net_avg_win | 33.2704 |
| net_avg_loss | -64.4248 |
| avg_hold_time_bars | 6.0897 |
| exposure | 0.0803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
