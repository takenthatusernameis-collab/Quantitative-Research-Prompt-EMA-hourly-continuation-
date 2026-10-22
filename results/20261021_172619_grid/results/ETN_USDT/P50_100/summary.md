# EMA Hourly Continuation — ETN/USDT P50_100

**Symbol:** ETN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.5267 |
| net_win_rate | 0.4035 |
| gross_profit_factor | 0.6684 |
| gross_win_rate | 0.4035 |
| sharpe_ratio | -3.6389 |
| sortino_ratio | -0.9481 |
| max_drawdown | 0.6185 |
| cagr | -0.3553 |
| net_avg_win | 58.2963 |
| net_avg_loss | -74.8767 |
| avg_hold_time_bars | 8.9193 |
| exposure | 0.1381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
