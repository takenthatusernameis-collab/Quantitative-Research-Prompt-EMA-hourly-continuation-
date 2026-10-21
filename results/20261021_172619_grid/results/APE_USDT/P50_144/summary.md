# EMA Hourly Continuation — APE/USDT P50_144

**Symbol:** APE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.8063 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9968 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.1918 |
| sortino_ratio | -0.3125 |
| max_drawdown | 0.3051 |
| cagr | -0.1349 |
| net_avg_win | 75.6146 |
| net_avg_loss | -94.3377 |
| avg_hold_time_bars | 20.3642 |
| exposure | 0.3101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
