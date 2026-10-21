# EMA Hourly Continuation — HBAR/USDT P21_55

**Symbol:** HBAR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.8146 |
| net_win_rate | 0.5289 |
| gross_profit_factor | 1.1136 |
| gross_win_rate | 0.5289 |
| sharpe_ratio | -1.3775 |
| sortino_ratio | -0.4299 |
| max_drawdown | 0.4065 |
| cagr | -0.1792 |
| net_avg_win | 69.5458 |
| net_avg_loss | -95.8514 |
| avg_hold_time_bars | 8.5482 |
| exposure | 0.1815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
