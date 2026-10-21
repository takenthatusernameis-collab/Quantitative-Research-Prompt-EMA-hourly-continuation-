# EMA Hourly Continuation — POLYX/USDT P12_144

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.8503 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.0446 |
| gross_win_rate | 0.5141 |
| sharpe_ratio | -0.9864 |
| sortino_ratio | -0.2796 |
| max_drawdown | 0.3363 |
| cagr | -0.1230 |
| net_avg_win | 79.3422 |
| net_avg_loss | -98.7155 |
| avg_hold_time_bars | 37.3376 |
| exposure | 0.6636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
