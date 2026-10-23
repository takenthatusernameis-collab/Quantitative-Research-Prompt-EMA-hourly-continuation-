# EMA Hourly Continuation — OSMO/USDT P89_200

**Symbol:** OSMO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.4921 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.7469 |
| gross_win_rate | 0.4254 |
| sharpe_ratio | -4.1115 |
| sortino_ratio | -1.0895 |
| max_drawdown | 0.7443 |
| cagr | -0.4086 |
| net_avg_win | 47.6514 |
| net_avg_loss | -70.0326 |
| avg_hold_time_bars | 13.0366 |
| exposure | 0.2104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
