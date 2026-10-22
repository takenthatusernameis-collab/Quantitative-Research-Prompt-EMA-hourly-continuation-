# EMA Hourly Continuation — SHIB/USDT P12_50

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1108 |
| net_profit_factor | 0.5196 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.9415 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -8.0544 |
| sortino_ratio | -3.7649 |
| max_drawdown | 0.9915 |
| cagr | -0.8469 |
| net_avg_win | 21.3079 |
| net_avg_loss | -34.0960 |
| avg_hold_time_bars | 6.4819 |
| exposure | 0.3265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
