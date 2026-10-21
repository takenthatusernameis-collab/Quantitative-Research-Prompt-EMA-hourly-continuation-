# EMA Hourly Continuation — IMX/USDT P55_144

**Symbol:** IMX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8224 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0167 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -0.9867 |
| sortino_ratio | -0.2653 |
| max_drawdown | 0.3368 |
| cagr | -0.1165 |
| net_avg_win | 69.0257 |
| net_avg_loss | -87.8358 |
| avg_hold_time_bars | 14.6108 |
| exposure | 0.2327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
