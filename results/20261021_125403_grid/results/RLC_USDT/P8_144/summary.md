# EMA Hourly Continuation — RLC/USDT P8_144

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.8767 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0681 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -0.8395 |
| sortino_ratio | -0.2400 |
| max_drawdown | 0.4045 |
| cagr | -0.1076 |
| net_avg_win | 86.2306 |
| net_avg_loss | -105.0235 |
| avg_hold_time_bars | 41.3123 |
| exposure | 0.7455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
