# EMA Hourly Continuation — DASH/USDT P100_144

**Symbol:** DASH/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.5764 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.7893 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -2.3834 |
| sortino_ratio | -0.4861 |
| max_drawdown | 0.4431 |
| cagr | -0.2009 |
| net_avg_win | 64.3823 |
| net_avg_loss | -89.1624 |
| avg_hold_time_bars | 6.0390 |
| exposure | 0.0563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
