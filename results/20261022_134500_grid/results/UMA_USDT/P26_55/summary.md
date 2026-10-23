# EMA Hourly Continuation — UMA/USDT P26_55

**Symbol:** UMA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.4808 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.9001 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -6.5740 |
| sortino_ratio | -2.7571 |
| max_drawdown | 0.9641 |
| cagr | -0.7319 |
| net_avg_win | 22.4098 |
| net_avg_loss | -39.2230 |
| avg_hold_time_bars | 5.4064 |
| exposure | 0.2140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
