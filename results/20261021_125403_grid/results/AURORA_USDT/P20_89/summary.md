# EMA Hourly Continuation — AURORA/USDT P20_89

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7241 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.2339 |
| sortino_ratio | -0.6473 |
| max_drawdown | 0.5614 |
| cagr | -0.2570 |
| net_avg_win | 69.3620 |
| net_avg_loss | -89.4891 |
| avg_hold_time_bars | 19.9466 |
| exposure | 0.3735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
