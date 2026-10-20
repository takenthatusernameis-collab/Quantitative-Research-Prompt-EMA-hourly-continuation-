# EMA Hourly Continuation — SSV/USDT P21_200

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.7012 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9453 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -2.0759 |
| sortino_ratio | -0.5492 |
| max_drawdown | 0.5157 |
| cagr | -0.2270 |
| net_avg_win | 65.5824 |
| net_avg_loss | -88.3557 |
| avg_hold_time_bars | 41.4886 |
| exposure | 0.6608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
