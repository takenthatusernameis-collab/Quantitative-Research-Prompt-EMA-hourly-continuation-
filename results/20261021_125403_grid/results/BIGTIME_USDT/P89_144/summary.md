# EMA Hourly Continuation — BIGTIME/USDT P89_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.6808 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9025 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -2.1358 |
| sortino_ratio | -0.5406 |
| max_drawdown | 0.4769 |
| cagr | -0.2192 |
| net_avg_win | 65.6032 |
| net_avg_loss | -88.1800 |
| avg_hold_time_bars | 7.4462 |
| exposure | 0.1065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
