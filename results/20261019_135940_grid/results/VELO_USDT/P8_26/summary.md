# EMA Hourly Continuation — VELO/USDT P8_26

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1595 |
| net_profit_factor | 0.5201 |
| net_win_rate | 0.4445 |
| gross_profit_factor | 0.8062 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -9.1744 |
| sortino_ratio | -5.1466 |
| max_drawdown | 0.9983 |
| cagr | -0.9196 |
| net_avg_win | 15.2591 |
| net_avg_loss | -23.4773 |
| avg_hold_time_bars | 3.6370 |
| exposure | 0.2637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
