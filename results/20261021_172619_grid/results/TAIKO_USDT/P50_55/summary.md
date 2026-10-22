# EMA Hourly Continuation — TAIKO/USDT P50_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 119 |
| net_profit_factor | 0.4730 |
| net_win_rate | 0.4202 |
| gross_profit_factor | 0.7221 |
| gross_win_rate | 0.4202 |
| sharpe_ratio | -2.5751 |
| sortino_ratio | -0.4125 |
| max_drawdown | 0.3836 |
| cagr | -0.1747 |
| net_avg_win | 65.7596 |
| net_avg_loss | -100.7457 |
| avg_hold_time_bars | 5.0084 |
| exposure | 0.0286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
