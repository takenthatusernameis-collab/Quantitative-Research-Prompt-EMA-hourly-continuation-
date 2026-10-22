# EMA Hourly Continuation — ATOM/USDT P50_144

**Symbol:** ATOM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6414 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0159 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -2.6908 |
| sortino_ratio | -0.8097 |
| max_drawdown | 0.6345 |
| cagr | -0.3213 |
| net_avg_win | 48.1780 |
| net_avg_loss | -77.4579 |
| avg_hold_time_bars | 12.3363 |
| exposure | 0.2551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
