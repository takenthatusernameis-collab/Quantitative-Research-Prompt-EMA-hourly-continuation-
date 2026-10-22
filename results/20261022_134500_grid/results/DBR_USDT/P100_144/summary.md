# EMA Hourly Continuation — DBR/USDT P100_144

**Symbol:** DBR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.3446 |
| net_win_rate | 0.4111 |
| gross_profit_factor | 0.7054 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -6.2550 |
| sortino_ratio | -1.8366 |
| max_drawdown | 0.8409 |
| cagr | -0.5998 |
| net_avg_win | 31.3596 |
| net_avg_loss | -63.5170 |
| avg_hold_time_bars | 9.4665 |
| exposure | 0.1846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
