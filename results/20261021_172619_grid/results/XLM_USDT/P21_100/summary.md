# EMA Hourly Continuation — XLM/USDT P21_100

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.8339 |
| net_win_rate | 0.5308 |
| gross_profit_factor | 1.1234 |
| gross_win_rate | 0.5308 |
| sharpe_ratio | -1.0775 |
| sortino_ratio | -0.3259 |
| max_drawdown | 0.3604 |
| cagr | -0.1404 |
| net_avg_win | 68.1243 |
| net_avg_loss | -92.4008 |
| avg_hold_time_bars | 20.7449 |
| exposure | 0.4140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
