# EMA Hourly Continuation — COTI/USDT P50_144

**Symbol:** COTI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6858 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 0.9899 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -2.2692 |
| sortino_ratio | -0.7323 |
| max_drawdown | 0.5829 |
| cagr | -0.2938 |
| net_avg_win | 47.8037 |
| net_avg_loss | -73.2848 |
| avg_hold_time_bars | 11.5665 |
| exposure | 0.2729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
