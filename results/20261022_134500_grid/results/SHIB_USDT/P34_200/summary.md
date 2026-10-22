# EMA Hourly Continuation — SHIB/USDT P34_200

**Symbol:** SHIB/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6548 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 1.0198 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -2.5916 |
| sortino_ratio | -0.6916 |
| max_drawdown | 0.5773 |
| cagr | -0.2848 |
| net_avg_win | 59.9872 |
| net_avg_loss | -90.1036 |
| avg_hold_time_bars | 30.5069 |
| exposure | 0.5034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
