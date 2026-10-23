# EMA Hourly Continuation — ELON/USDT P55_144

**Symbol:** ELON/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.4545 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.7074 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -4.8096 |
| sortino_ratio | -1.5316 |
| max_drawdown | 0.8389 |
| cagr | -0.5105 |
| net_avg_win | 31.8641 |
| net_avg_loss | -54.0051 |
| avg_hold_time_bars | 10.5649 |
| exposure | 0.2406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
