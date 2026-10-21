# EMA Hourly Continuation — RLC/USDT P20_55

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.7020 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -2.8128 |
| sortino_ratio | -0.9699 |
| max_drawdown | 0.6855 |
| cagr | -0.3590 |
| net_avg_win | 55.6038 |
| net_avg_loss | -76.2628 |
| avg_hold_time_bars | 7.7453 |
| exposure | 0.2045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
