# EMA Hourly Continuation — AAVE/USDT P21_89

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.7999 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9881 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.4188 |
| sortino_ratio | -0.4282 |
| max_drawdown | 0.4374 |
| cagr | -0.1799 |
| net_avg_win | 70.6291 |
| net_avg_loss | -88.2983 |
| avg_hold_time_bars | 17.2252 |
| exposure | 0.3476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
