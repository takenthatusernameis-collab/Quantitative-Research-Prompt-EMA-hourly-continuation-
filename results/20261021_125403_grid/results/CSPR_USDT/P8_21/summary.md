# EMA Hourly Continuation — CSPR/USDT P8_21

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.5425 |
| net_win_rate | 0.4148 |
| gross_profit_factor | 0.7127 |
| gross_win_rate | 0.4148 |
| sharpe_ratio | -4.0551 |
| sortino_ratio | -1.2296 |
| max_drawdown | 0.7599 |
| cagr | -0.4334 |
| net_avg_win | 47.4304 |
| net_avg_loss | -61.9797 |
| avg_hold_time_bars | 5.7467 |
| exposure | 0.1196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
