# EMA Hourly Continuation — VR/USDT P21_144

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.4499 |
| net_win_rate | 0.3282 |
| gross_profit_factor | 0.6565 |
| gross_win_rate | 0.3389 |
| sharpe_ratio | -9.7527 |
| sortino_ratio | -3.4677 |
| max_drawdown | 0.9931 |
| cagr | -0.8624 |
| net_avg_win | 37.7845 |
| net_avg_loss | -41.0341 |
| avg_hold_time_bars | 16.4672 |
| exposure | 0.4903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
