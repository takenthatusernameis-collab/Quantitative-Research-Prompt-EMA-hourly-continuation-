# EMA Hourly Continuation — AXS/USDT P8_21

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1614 |
| net_profit_factor | 0.2573 |
| net_win_rate | 0.4281 |
| gross_profit_factor | 0.6458 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -12.0992 |
| sortino_ratio | -6.8582 |
| max_drawdown | 0.9998 |
| cagr | -0.9688 |
| net_avg_win | 5.0137 |
| net_avg_loss | -14.5860 |
| avg_hold_time_bars | 3.0322 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
