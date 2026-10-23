# EMA Hourly Continuation — RIO/USDT P8_34

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1508 |
| net_profit_factor | 0.5477 |
| net_win_rate | 0.4251 |
| gross_profit_factor | 0.8095 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -8.6676 |
| sortino_ratio | -4.7153 |
| max_drawdown | 0.9969 |
| cagr | -0.9016 |
| net_avg_win | 18.8294 |
| net_avg_loss | -25.4191 |
| avg_hold_time_bars | 4.8422 |
| exposure | 0.3352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
