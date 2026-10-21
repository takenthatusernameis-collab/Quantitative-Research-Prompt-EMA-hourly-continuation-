# EMA Hourly Continuation — AXL/USDT P21_100

**Symbol:** AXL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6476 |
| net_win_rate | 0.4291 |
| gross_profit_factor | 0.7904 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -3.6839 |
| sortino_ratio | -1.2257 |
| max_drawdown | 0.7651 |
| cagr | -0.4335 |
| net_avg_win | 58.5462 |
| net_avg_loss | -67.9492 |
| avg_hold_time_bars | 14.5224 |
| exposure | 0.3660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
