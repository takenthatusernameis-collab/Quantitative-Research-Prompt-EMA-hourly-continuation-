# EMA Hourly Continuation — POL/USDT P100_144

**Symbol:** POL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.6247 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.8953 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -2.1200 |
| sortino_ratio | -0.4709 |
| max_drawdown | 0.4348 |
| cagr | -0.1935 |
| net_avg_win | 60.4043 |
| net_avg_loss | -88.9571 |
| avg_hold_time_bars | 6.6167 |
| exposure | 0.0722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
