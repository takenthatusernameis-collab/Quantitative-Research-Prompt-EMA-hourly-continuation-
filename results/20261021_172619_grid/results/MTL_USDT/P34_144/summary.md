# EMA Hourly Continuation — MTL/USDT P34_144

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.6386 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8430 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -2.7891 |
| sortino_ratio | -0.7491 |
| max_drawdown | 0.5838 |
| cagr | -0.2919 |
| net_avg_win | 63.0134 |
| net_avg_loss | -82.0667 |
| avg_hold_time_bars | 28.5432 |
| exposure | 0.4637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
