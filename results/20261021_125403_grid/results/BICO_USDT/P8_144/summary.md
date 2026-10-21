# EMA Hourly Continuation — BICO/USDT P8_144

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.9576 |
| net_win_rate | 0.5317 |
| gross_profit_factor | 1.1169 |
| gross_win_rate | 0.5317 |
| sharpe_ratio | -0.1990 |
| sortino_ratio | -0.0546 |
| max_drawdown | 0.2357 |
| cagr | -0.0307 |
| net_avg_win | 88.0284 |
| net_avg_loss | -104.3625 |
| avg_hold_time_bars | 45.5895 |
| exposure | 0.7522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
