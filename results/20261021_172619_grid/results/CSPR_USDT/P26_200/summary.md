# EMA Hourly Continuation — CSPR/USDT P26_200

**Symbol:** CSPR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.7061 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8567 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -2.2789 |
| sortino_ratio | -0.6680 |
| max_drawdown | 0.5527 |
| cagr | -0.2651 |
| net_avg_win | 66.0192 |
| net_avg_loss | -79.3343 |
| avg_hold_time_bars | 25.8478 |
| exposure | 0.5017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
