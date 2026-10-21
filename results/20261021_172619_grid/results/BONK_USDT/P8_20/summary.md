# EMA Hourly Continuation — BONK/USDT P8_20

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.7828 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0068 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.6957 |
| sortino_ratio | -0.5229 |
| max_drawdown | 0.5281 |
| cagr | -0.2139 |
| net_avg_win | 70.4686 |
| net_avg_loss | -90.8039 |
| avg_hold_time_bars | 5.3810 |
| exposure | 0.1130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
