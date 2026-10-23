# EMA Hourly Continuation — VELO/USDT P8_21

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1709 |
| net_profit_factor | 0.5263 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -10.0755 |
| sortino_ratio | -5.8585 |
| max_drawdown | 0.9993 |
| cagr | -0.9441 |
| net_avg_win | 14.5880 |
| net_avg_loss | -22.2514 |
| avg_hold_time_bars | 2.7929 |
| exposure | 0.2170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
