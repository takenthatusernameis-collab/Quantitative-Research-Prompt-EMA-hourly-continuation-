# EMA Hourly Continuation — BIGTIME/USDT P26_55

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.7353 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9854 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -2.2461 |
| sortino_ratio | -0.7296 |
| max_drawdown | 0.5968 |
| cagr | -0.2838 |
| net_avg_win | 61.5353 |
| net_avg_loss | -83.3596 |
| avg_hold_time_bars | 7.5515 |
| exposure | 0.1760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
