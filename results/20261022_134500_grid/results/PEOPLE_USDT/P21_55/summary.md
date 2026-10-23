# EMA Hourly Continuation — PEOPLE/USDT P21_55

**Symbol:** PEOPLE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 916 |
| net_profit_factor | 0.5652 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8529 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -5.6545 |
| sortino_ratio | -2.4154 |
| max_drawdown | 0.9443 |
| cagr | -0.6817 |
| net_avg_win | 29.2266 |
| net_avg_loss | -43.7865 |
| avg_hold_time_bars | 5.3024 |
| exposure | 0.2198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
