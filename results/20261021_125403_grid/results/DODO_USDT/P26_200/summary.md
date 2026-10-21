# EMA Hourly Continuation — DODO/USDT P26_200

**Symbol:** DODO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.6806 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8226 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -2.4231 |
| sortino_ratio | -0.6666 |
| max_drawdown | 0.5619 |
| cagr | -0.2641 |
| net_avg_win | 67.5024 |
| net_avg_loss | -80.6761 |
| avg_hold_time_bars | 30.1319 |
| exposure | 0.5168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
