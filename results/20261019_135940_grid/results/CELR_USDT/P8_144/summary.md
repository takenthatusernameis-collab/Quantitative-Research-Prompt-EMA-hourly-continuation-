# EMA Hourly Continuation — CELR/USDT P8_144

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6409 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.8317 |
| sortino_ratio | -0.8123 |
| max_drawdown | 0.6346 |
| cagr | -0.3213 |
| net_avg_win | 57.0914 |
| net_avg_loss | -76.8644 |
| avg_hold_time_bars | 40.3159 |
| exposure | 0.7680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
