# EMA Hourly Continuation — BTT/USDT P50_144

**Symbol:** BTT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.5428 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8600 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -3.9503 |
| sortino_ratio | -1.0128 |
| max_drawdown | 0.6996 |
| cagr | -0.3797 |
| net_avg_win | 57.5997 |
| net_avg_loss | -85.8418 |
| avg_hold_time_bars | 21.1646 |
| exposure | 0.3098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
