# EMA Hourly Continuation — AUCTION/USDT P89_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.4245 |
| net_win_rate | 0.4171 |
| gross_profit_factor | 0.7063 |
| gross_win_rate | 0.4218 |
| sharpe_ratio | -5.4167 |
| sortino_ratio | -1.5322 |
| max_drawdown | 0.8662 |
| cagr | -0.5489 |
| net_avg_win | 36.2795 |
| net_avg_loss | -61.1492 |
| avg_hold_time_bars | 12.3649 |
| exposure | 0.2362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
