# EMA Hourly Continuation — TRADE/USDT P21_26

**Symbol:** TRADE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.2383 |
| net_win_rate | 0.3156 |
| gross_profit_factor | 0.6101 |
| gross_win_rate | 0.3443 |
| sharpe_ratio | -13.5990 |
| sortino_ratio | -6.0648 |
| max_drawdown | 0.9997 |
| cagr | -0.9621 |
| net_avg_win | 10.5658 |
| net_avg_loss | -20.4436 |
| avg_hold_time_bars | 3.0362 |
| exposure | 0.1295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
