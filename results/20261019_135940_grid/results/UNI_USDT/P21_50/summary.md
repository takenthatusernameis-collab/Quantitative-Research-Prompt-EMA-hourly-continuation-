# EMA Hourly Continuation — UNI/USDT P21_50

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.4489 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -7.8325 |
| sortino_ratio | -3.5114 |
| max_drawdown | 0.9879 |
| cagr | -0.8261 |
| net_avg_win | 17.6445 |
| net_avg_loss | -31.6646 |
| avg_hold_time_bars | 4.0489 |
| exposure | 0.1881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
