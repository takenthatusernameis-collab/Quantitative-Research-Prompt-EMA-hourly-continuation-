# EMA Hourly Continuation — STRK/USDT P50_100

**Symbol:** STRK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8462 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0664 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -0.9518 |
| sortino_ratio | -0.2548 |
| max_drawdown | 0.3185 |
| cagr | -0.1121 |
| net_avg_win | 79.3259 |
| net_avg_loss | -100.4822 |
| avg_hold_time_bars | 8.0405 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
