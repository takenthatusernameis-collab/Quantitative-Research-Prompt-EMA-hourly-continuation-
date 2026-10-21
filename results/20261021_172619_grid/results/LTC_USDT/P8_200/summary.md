# EMA Hourly Continuation — LTC/USDT P8_200

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6355 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8172 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -2.2869 |
| sortino_ratio | -0.5636 |
| max_drawdown | 0.4959 |
| cagr | -0.2282 |
| net_avg_win | 60.8702 |
| net_avg_loss | -80.0081 |
| avg_hold_time_bars | 55.1694 |
| exposure | 0.7548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
