# EMA Hourly Continuation — POPCAT/USDT P8_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.8874 |
| net_win_rate | 0.5353 |
| gross_profit_factor | 1.1720 |
| gross_win_rate | 0.5412 |
| sharpe_ratio | -0.8416 |
| sortino_ratio | -0.2369 |
| max_drawdown | 0.3974 |
| cagr | -0.1098 |
| net_avg_win | 96.1947 |
| net_avg_loss | -124.8705 |
| avg_hold_time_bars | 44.2412 |
| exposure | 0.7946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
