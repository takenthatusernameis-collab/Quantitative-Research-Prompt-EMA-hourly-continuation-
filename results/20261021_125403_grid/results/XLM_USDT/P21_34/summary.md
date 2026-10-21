# EMA Hourly Continuation — XLM/USDT P21_34

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.5301 |
| gross_profit_factor | 1.1266 |
| gross_win_rate | 0.5301 |
| sharpe_ratio | -1.4686 |
| sortino_ratio | -0.3353 |
| max_drawdown | 0.3444 |
| cagr | -0.1414 |
| net_avg_win | 67.5777 |
| net_avg_loss | -103.4345 |
| avg_hold_time_bars | 5.7108 |
| exposure | 0.0646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
