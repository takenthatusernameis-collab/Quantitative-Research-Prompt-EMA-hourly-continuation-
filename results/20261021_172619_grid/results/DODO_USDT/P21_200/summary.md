# EMA Hourly Continuation — DODO/USDT P21_200

**Symbol:** DODO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6829 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.8249 |
| gross_win_rate | 0.4466 |
| sharpe_ratio | -2.4269 |
| sortino_ratio | -0.6549 |
| max_drawdown | 0.5655 |
| cagr | -0.2601 |
| net_avg_win | 70.3197 |
| net_avg_loss | -83.0949 |
| avg_hold_time_bars | 35.3123 |
| exposure | 0.5832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
