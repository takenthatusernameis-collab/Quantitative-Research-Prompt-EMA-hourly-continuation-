# EMA Hourly Continuation — FET/USDT P26_34

**Symbol:** FET/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1069 |
| net_profit_factor | 0.3233 |
| net_win_rate | 0.3966 |
| gross_profit_factor | 0.7541 |
| gross_win_rate | 0.4219 |
| sharpe_ratio | -11.6222 |
| sortino_ratio | -5.4497 |
| max_drawdown | 0.9992 |
| cagr | -0.9418 |
| net_avg_win | 11.2581 |
| net_avg_loss | -22.8923 |
| avg_hold_time_bars | 1.8297 |
| exposure | 0.0889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
