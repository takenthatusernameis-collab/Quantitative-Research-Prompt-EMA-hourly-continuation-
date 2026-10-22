# EMA Hourly Continuation — MTL/USDT P12_144

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8294 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0651 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -1.2311 |
| sortino_ratio | -0.3402 |
| max_drawdown | 0.4137 |
| cagr | -0.1469 |
| net_avg_win | 83.6236 |
| net_avg_loss | -106.3636 |
| avg_hold_time_bars | 41.3182 |
| exposure | 0.6993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
