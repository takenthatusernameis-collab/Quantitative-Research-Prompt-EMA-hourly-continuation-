# EMA Hourly Continuation — XPR/USDT P21_100

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7243 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9161 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -2.1434 |
| sortino_ratio | -0.6129 |
| max_drawdown | 0.5174 |
| cagr | -0.2457 |
| net_avg_win | 69.4373 |
| net_avg_loss | -87.2334 |
| avg_hold_time_bars | 16.1514 |
| exposure | 0.2959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
