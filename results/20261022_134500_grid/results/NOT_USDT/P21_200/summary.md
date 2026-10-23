# EMA Hourly Continuation — NOT/USDT P21_200

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.5518 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.7421 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -3.6846 |
| sortino_ratio | -1.0340 |
| max_drawdown | 0.7081 |
| cagr | -0.3881 |
| net_avg_win | 52.3237 |
| net_avg_loss | -70.0446 |
| avg_hold_time_bars | 34.6580 |
| exposure | 0.6284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
