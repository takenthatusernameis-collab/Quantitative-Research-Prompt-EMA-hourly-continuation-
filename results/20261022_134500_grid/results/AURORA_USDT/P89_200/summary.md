# EMA Hourly Continuation — AURORA/USDT P89_200

**Symbol:** AURORA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.5713 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -3.2064 |
| sortino_ratio | -0.8263 |
| max_drawdown | 0.6297 |
| cagr | -0.3232 |
| net_avg_win | 54.4218 |
| net_avg_loss | -81.8795 |
| avg_hold_time_bars | 11.2659 |
| exposure | 0.1695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
