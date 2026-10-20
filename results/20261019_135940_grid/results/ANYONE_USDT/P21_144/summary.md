# EMA Hourly Continuation — ANYONE/USDT P21_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7207 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9154 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.0805 |
| sortino_ratio | -0.6050 |
| max_drawdown | 0.4974 |
| cagr | -0.2514 |
| net_avg_win | 66.9639 |
| net_avg_loss | -85.0971 |
| avg_hold_time_bars | 27.5866 |
| exposure | 0.5395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
