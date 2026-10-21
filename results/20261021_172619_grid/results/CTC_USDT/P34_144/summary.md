# EMA Hourly Continuation — CTC/USDT P34_144

**Symbol:** CTC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8228 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0559 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.2208 |
| sortino_ratio | -0.3524 |
| max_drawdown | 0.4343 |
| cagr | -0.1513 |
| net_avg_win | 75.3913 |
| net_avg_loss | -97.2356 |
| avg_hold_time_bars | 18.3639 |
| exposure | 0.3372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
