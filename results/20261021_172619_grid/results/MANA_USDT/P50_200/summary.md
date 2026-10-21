# EMA Hourly Continuation — MANA/USDT P50_200

**Symbol:** MANA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8444 |
| net_win_rate | 0.5160 |
| gross_profit_factor | 1.0491 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -0.8115 |
| sortino_ratio | -0.1955 |
| max_drawdown | 0.2374 |
| cagr | -0.0877 |
| net_avg_win | 77.0834 |
| net_avg_loss | -97.3245 |
| avg_hold_time_bars | 34.5196 |
| exposure | 0.4409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
