# EMA Hourly Continuation — BONK/USDT P8_144

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6611 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -3.0141 |
| sortino_ratio | -0.9321 |
| max_drawdown | 0.7047 |
| cagr | -0.3623 |
| net_avg_win | 56.6730 |
| net_avg_loss | -78.3269 |
| avg_hold_time_bars | 33.7193 |
| exposure | 0.7480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
