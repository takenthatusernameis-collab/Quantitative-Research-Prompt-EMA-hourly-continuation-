# EMA Hourly Continuation — INJ/USDT P55_200

**Symbol:** INJ/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.5310 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.7535 |
| gross_win_rate | 0.4383 |
| sharpe_ratio | -3.6411 |
| sortino_ratio | -0.9878 |
| max_drawdown | 0.7129 |
| cagr | -0.3839 |
| net_avg_win | 47.9919 |
| net_avg_loss | -69.7833 |
| avg_hold_time_bars | 18.8845 |
| exposure | 0.3270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
