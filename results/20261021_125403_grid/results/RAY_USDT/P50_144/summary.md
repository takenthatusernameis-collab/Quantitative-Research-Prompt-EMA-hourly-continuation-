# EMA Hourly Continuation — RAY/USDT P50_144

**Symbol:** RAY/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7521 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9285 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -1.5981 |
| sortino_ratio | -0.4284 |
| max_drawdown | 0.4384 |
| cagr | -0.1800 |
| net_avg_win | 69.2386 |
| net_avg_loss | -87.4818 |
| avg_hold_time_bars | 15.3994 |
| exposure | 0.2471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
