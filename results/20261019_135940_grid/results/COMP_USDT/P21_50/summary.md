# EMA Hourly Continuation — COMP/USDT P21_50

**Symbol:** COMP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.3977 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8208 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -7.7766 |
| sortino_ratio | -3.6098 |
| max_drawdown | 0.9887 |
| cagr | -0.8297 |
| net_avg_win | 13.0780 |
| net_avg_loss | -28.2907 |
| avg_hold_time_bars | 4.8082 |
| exposure | 0.2358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
