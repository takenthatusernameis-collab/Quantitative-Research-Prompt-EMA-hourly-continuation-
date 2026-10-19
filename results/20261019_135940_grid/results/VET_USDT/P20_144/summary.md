# EMA Hourly Continuation — VET/USDT P20_144

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.6513 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9636 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.9048 |
| sortino_ratio | -0.9303 |
| max_drawdown | 0.6895 |
| cagr | -0.3576 |
| net_avg_win | 49.5154 |
| net_avg_loss | -73.4194 |
| avg_hold_time_bars | 22.8117 |
| exposure | 0.5340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
