# EMA Hourly Continuation — RUNE/USDT P8_144

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.9735 |
| net_win_rate | 0.5376 |
| gross_profit_factor | 1.1558 |
| gross_win_rate | 0.5376 |
| sharpe_ratio | -0.0890 |
| sortino_ratio | -0.0215 |
| max_drawdown | 0.1468 |
| cagr | -0.0148 |
| net_avg_win | 90.1958 |
| net_avg_loss | -107.7331 |
| avg_hold_time_bars | 62.5161 |
| exposure | 0.7928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
