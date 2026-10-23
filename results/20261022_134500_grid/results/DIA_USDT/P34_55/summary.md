# EMA Hourly Continuation — DIA/USDT P34_55

**Symbol:** DIA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 856 |
| net_profit_factor | 0.4076 |
| net_win_rate | 0.4124 |
| gross_profit_factor | 0.7858 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -8.4081 |
| sortino_ratio | -3.4666 |
| max_drawdown | 0.9869 |
| cagr | -0.8208 |
| net_avg_win | 19.2400 |
| net_avg_loss | -33.1232 |
| avg_hold_time_bars | 3.8984 |
| exposure | 0.1510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
