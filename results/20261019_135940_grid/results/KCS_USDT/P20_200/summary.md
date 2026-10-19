# EMA Hourly Continuation — KCS/USDT P20_200

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.4440 |
| net_win_rate | 0.4034 |
| gross_profit_factor | 0.9319 |
| gross_win_rate | 0.4352 |
| sharpe_ratio | -6.0571 |
| sortino_ratio | -1.7297 |
| max_drawdown | 0.8889 |
| cagr | -0.5831 |
| net_avg_win | 43.0244 |
| net_avg_loss | -65.5230 |
| avg_hold_time_bars | 33.3765 |
| exposure | 0.6205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
