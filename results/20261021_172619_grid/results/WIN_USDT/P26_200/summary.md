# EMA Hourly Continuation — WIN/USDT P26_200

**Symbol:** WIN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8307 |
| net_win_rate | 0.5185 |
| gross_profit_factor | 1.0610 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -0.8700 |
| sortino_ratio | -0.2054 |
| max_drawdown | 0.3071 |
| cagr | -0.0919 |
| net_avg_win | 75.3330 |
| net_avg_loss | -97.6664 |
| avg_hold_time_bars | 43.4222 |
| exposure | 0.5329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
