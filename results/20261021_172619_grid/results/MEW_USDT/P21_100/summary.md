# EMA Hourly Continuation — MEW/USDT P21_100

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8087 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.3074 |
| sortino_ratio | -0.3994 |
| max_drawdown | 0.3919 |
| cagr | -0.1688 |
| net_avg_win | 68.8612 |
| net_avg_loss | -85.5280 |
| avg_hold_time_bars | 19.0901 |
| exposure | 0.3948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
