# EMA Hourly Continuation — OSMO/USDT P20_200

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7832 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0944 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -1.6617 |
| sortino_ratio | -0.4682 |
| max_drawdown | 0.4943 |
| cagr | -0.1985 |
| net_avg_win | 77.4100 |
| net_avg_loss | -100.8642 |
| avg_hold_time_bars | 35.7107 |
| exposure | 0.6395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
