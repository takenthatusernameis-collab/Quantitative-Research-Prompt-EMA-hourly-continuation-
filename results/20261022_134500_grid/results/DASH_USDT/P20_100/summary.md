# EMA Hourly Continuation — DASH/USDT P20_100

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.5384 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.9037 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -5.3037 |
| sortino_ratio | -1.9496 |
| max_drawdown | 0.9081 |
| cagr | -0.6053 |
| net_avg_win | 34.7667 |
| net_avg_loss | -52.3156 |
| avg_hold_time_bars | 13.7755 |
| exposure | 0.4239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
