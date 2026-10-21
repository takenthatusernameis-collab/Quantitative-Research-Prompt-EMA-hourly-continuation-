# EMA Hourly Continuation — NMR/USDT P50_200

**Symbol:** NMR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8442 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0668 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.8910 |
| sortino_ratio | -0.2348 |
| max_drawdown | 0.3009 |
| cagr | -0.1043 |
| net_avg_win | 74.8413 |
| net_avg_loss | -96.3635 |
| avg_hold_time_bars | 23.9315 |
| exposure | 0.3655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
