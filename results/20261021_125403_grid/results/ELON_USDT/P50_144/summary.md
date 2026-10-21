# EMA Hourly Continuation — ELON/USDT P50_144

**Symbol:** ELON/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5273 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.6803 |
| gross_win_rate | 0.4193 |
| sharpe_ratio | -3.4298 |
| sortino_ratio | -0.9121 |
| max_drawdown | 0.6565 |
| cagr | -0.3426 |
| net_avg_win | 49.0773 |
| net_avg_loss | -67.1999 |
| avg_hold_time_bars | 14.9348 |
| exposure | 0.2396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
