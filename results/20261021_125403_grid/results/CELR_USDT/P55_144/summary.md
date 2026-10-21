# EMA Hourly Continuation — CELR/USDT P55_144

**Symbol:** CELR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7567 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9563 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.6387 |
| sortino_ratio | -0.4521 |
| max_drawdown | 0.4243 |
| cagr | -0.1884 |
| net_avg_win | 69.2027 |
| net_avg_loss | -88.5660 |
| avg_hold_time_bars | 16.5508 |
| exposure | 0.2801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
