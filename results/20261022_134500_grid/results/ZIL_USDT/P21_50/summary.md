# EMA Hourly Continuation — ZIL/USDT P21_50

**Symbol:** ZIL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.4350 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -8.1198 |
| sortino_ratio | -3.6674 |
| max_drawdown | 0.9894 |
| cagr | -0.8335 |
| net_avg_win | 16.8829 |
| net_avg_loss | -31.0895 |
| avg_hold_time_bars | 4.4803 |
| exposure | 0.2065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
