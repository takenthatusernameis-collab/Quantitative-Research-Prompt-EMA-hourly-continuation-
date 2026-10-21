# EMA Hourly Continuation — TRAC/USDT P21_34

**Symbol:** TRAC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6855 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9642 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.1172 |
| sortino_ratio | -0.5698 |
| max_drawdown | 0.5040 |
| cagr | -0.2284 |
| net_avg_win | 59.9637 |
| net_avg_loss | -85.5035 |
| avg_hold_time_bars | 7.9233 |
| exposure | 0.1268 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
