# EMA Hourly Continuation — XMR/USDT P21_144

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.6942 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9000 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -2.5732 |
| sortino_ratio | -0.7882 |
| max_drawdown | 0.6095 |
| cagr | -0.3037 |
| net_avg_win | 62.4621 |
| net_avg_loss | -79.3706 |
| avg_hold_time_bars | 20.9309 |
| exposure | 0.4405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
