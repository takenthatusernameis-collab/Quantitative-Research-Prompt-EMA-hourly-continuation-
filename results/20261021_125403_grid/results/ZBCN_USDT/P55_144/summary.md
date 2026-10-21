# EMA Hourly Continuation — ZBCN/USDT P55_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.9713 |
| net_win_rate | 0.5380 |
| gross_profit_factor | 1.1487 |
| gross_win_rate | 0.5380 |
| sharpe_ratio | -0.1138 |
| sortino_ratio | -0.0301 |
| max_drawdown | 0.2340 |
| cagr | -0.0196 |
| net_avg_win | 91.0978 |
| net_avg_loss | -109.2129 |
| avg_hold_time_bars | 11.5228 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
