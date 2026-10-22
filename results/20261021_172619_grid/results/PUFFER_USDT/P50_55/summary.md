# EMA Hourly Continuation — PUFFER/USDT P50_55

**Symbol:** PUFFER/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 115 |
| net_profit_factor | 0.8912 |
| net_win_rate | 0.5478 |
| gross_profit_factor | 1.2173 |
| gross_win_rate | 0.5478 |
| sharpe_ratio | -0.4189 |
| sortino_ratio | -0.0728 |
| max_drawdown | 0.1622 |
| cagr | -0.0338 |
| net_avg_win | 87.2132 |
| net_avg_loss | -118.5651 |
| avg_hold_time_bars | 7.6870 |
| exposure | 0.0500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
