# EMA Hourly Continuation — AIOZ/USDT P55_144

**Symbol:** AIOZ/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.8462 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0308 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.0608 |
| sortino_ratio | -0.2862 |
| max_drawdown | 0.3498 |
| cagr | -0.1250 |
| net_avg_win | 87.5680 |
| net_avg_loss | -105.8500 |
| avg_hold_time_bars | 14.7119 |
| exposure | 0.2367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
