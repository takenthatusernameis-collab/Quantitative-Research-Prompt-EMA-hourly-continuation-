# EMA Hourly Continuation — MTL/USDT P12_144

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.7237 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0716 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -2.3320 |
| sortino_ratio | -0.6924 |
| max_drawdown | 0.5687 |
| cagr | -0.2802 |
| net_avg_win | 66.7927 |
| net_avg_loss | -92.2958 |
| avg_hold_time_bars | 35.1946 |
| exposure | 0.7040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
