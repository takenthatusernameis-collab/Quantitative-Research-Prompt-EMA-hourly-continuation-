# EMA Hourly Continuation — TRB/USDT P34_89

**Symbol:** TRB/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.6603 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -2.6469 |
| sortino_ratio | -0.7582 |
| max_drawdown | 0.6024 |
| cagr | -0.2938 |
| net_avg_win | 60.0699 |
| net_avg_loss | -79.2390 |
| avg_hold_time_bars | 12.7241 |
| exposure | 0.2338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
