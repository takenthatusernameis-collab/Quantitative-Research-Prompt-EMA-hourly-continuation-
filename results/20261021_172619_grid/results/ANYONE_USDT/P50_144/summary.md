# EMA Hourly Continuation — ANYONE/USDT P50_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.8221 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -1.0090 |
| sortino_ratio | -0.2643 |
| max_drawdown | 0.3359 |
| cagr | -0.1164 |
| net_avg_win | 75.6693 |
| net_avg_loss | -89.6348 |
| avg_hold_time_bars | 16.4470 |
| exposure | 0.2510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
