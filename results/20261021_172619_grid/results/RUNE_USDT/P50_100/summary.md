# EMA Hourly Continuation — RUNE/USDT P50_100

**Symbol:** RUNE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7815 |
| net_win_rate | 0.5206 |
| gross_profit_factor | 1.0387 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -1.2067 |
| sortino_ratio | -0.3206 |
| max_drawdown | 0.4138 |
| cagr | -0.1368 |
| net_avg_win | 62.4046 |
| net_avg_loss | -86.7106 |
| avg_hold_time_bars | 11.1676 |
| exposure | 0.1726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
