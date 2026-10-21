# EMA Hourly Continuation — BONK/USDT P21_26

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 142 |
| net_profit_factor | 0.8520 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.1129 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -0.5866 |
| sortino_ratio | -0.1008 |
| max_drawdown | 0.1692 |
| cagr | -0.0463 |
| net_avg_win | 86.1530 |
| net_avg_loss | -113.1942 |
| avg_hold_time_bars | 5.7254 |
| exposure | 0.0370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
