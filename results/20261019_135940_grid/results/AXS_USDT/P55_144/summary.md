# EMA Hourly Continuation — AXS/USDT P55_144

**Symbol:** AXS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7390 |
| net_win_rate | 0.5268 |
| gross_profit_factor | 1.1321 |
| gross_win_rate | 0.5312 |
| sharpe_ratio | -2.0297 |
| sortino_ratio | -0.6087 |
| max_drawdown | 0.5550 |
| cagr | -0.2504 |
| net_avg_win | 61.9927 |
| net_avg_loss | -93.3851 |
| avg_hold_time_bars | 11.7500 |
| exposure | 0.2382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
