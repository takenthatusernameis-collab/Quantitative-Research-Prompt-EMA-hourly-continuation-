# EMA Hourly Continuation — FIDA/USDT P26_100

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.5731 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8837 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -4.3462 |
| sortino_ratio | -1.5780 |
| max_drawdown | 0.8567 |
| cagr | -0.5290 |
| net_avg_win | 36.9377 |
| net_avg_loss | -55.4784 |
| avg_hold_time_bars | 11.7814 |
| exposure | 0.3561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
