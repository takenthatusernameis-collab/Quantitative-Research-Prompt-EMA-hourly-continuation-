# EMA Hourly Continuation — DUSK/USDT P12_21

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1419 |
| net_profit_factor | 0.4049 |
| net_win_rate | 0.4383 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -10.1814 |
| sortino_ratio | -5.4130 |
| max_drawdown | 0.9989 |
| cagr | -0.9333 |
| net_avg_win | 10.9248 |
| net_avg_loss | -21.0591 |
| avg_hold_time_bars | 2.5525 |
| exposure | 0.1646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
