# EMA Hourly Continuation — FLR/USDT P100_144

**Symbol:** FLR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.6045 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8659 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -2.4659 |
| sortino_ratio | -0.5186 |
| max_drawdown | 0.4509 |
| cagr | -0.2124 |
| net_avg_win | 69.6299 |
| net_avg_loss | -97.4571 |
| avg_hold_time_bars | 6.9074 |
| exposure | 0.0678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
