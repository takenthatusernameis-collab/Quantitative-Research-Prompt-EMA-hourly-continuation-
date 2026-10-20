# EMA Hourly Continuation — ROSE/USDT P144_200

**Symbol:** ROSE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.5647 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9570 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -3.3187 |
| sortino_ratio | -0.9129 |
| max_drawdown | 0.6665 |
| cagr | -0.3510 |
| net_avg_win | 47.4696 |
| net_avg_loss | -79.6631 |
| avg_hold_time_bars | 4.4489 |
| exposure | 0.0752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
