# EMA Hourly Continuation — ARKM/USDT P89_200

**Symbol:** ARKM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.5749 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8198 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -3.6598 |
| sortino_ratio | -1.0771 |
| max_drawdown | 0.7269 |
| cagr | -0.3990 |
| net_avg_win | 50.0372 |
| net_avg_loss | -71.0178 |
| avg_hold_time_bars | 10.3802 |
| exposure | 0.2048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
