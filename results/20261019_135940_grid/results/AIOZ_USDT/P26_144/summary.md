# EMA Hourly Continuation — AIOZ/USDT P26_144

**Symbol:** AIOZ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.6486 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9152 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -3.2851 |
| sortino_ratio | -1.0755 |
| max_drawdown | 0.7424 |
| cagr | -0.4033 |
| net_avg_win | 51.9897 |
| net_avg_loss | -72.5592 |
| avg_hold_time_bars | 19.2578 |
| exposure | 0.4753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
