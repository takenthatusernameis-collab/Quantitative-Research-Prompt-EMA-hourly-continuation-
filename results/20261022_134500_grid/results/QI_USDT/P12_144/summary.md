# EMA Hourly Continuation — QI/USDT P12_144

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6213 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8959 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -3.3640 |
| sortino_ratio | -1.0218 |
| max_drawdown | 0.7218 |
| cagr | -0.3840 |
| net_avg_win | 54.0710 |
| net_avg_loss | -73.0400 |
| avg_hold_time_bars | 30.7356 |
| exposure | 0.6523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
