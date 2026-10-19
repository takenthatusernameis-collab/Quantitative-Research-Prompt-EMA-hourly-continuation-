# EMA Hourly Continuation — FIL/USDT P26_55

**Symbol:** FIL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.4282 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -7.2310 |
| sortino_ratio | -3.0894 |
| max_drawdown | 0.9792 |
| cagr | -0.7825 |
| net_avg_win | 17.3991 |
| net_avg_loss | -34.2163 |
| avg_hold_time_bars | 3.8817 |
| exposure | 0.1625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
