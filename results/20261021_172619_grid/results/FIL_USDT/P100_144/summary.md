# EMA Hourly Continuation — FIL/USDT P100_144

**Symbol:** FIL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 192 |
| net_profit_factor | 0.7991 |
| net_win_rate | 0.5312 |
| gross_profit_factor | 1.1117 |
| gross_win_rate | 0.5312 |
| sharpe_ratio | -0.8803 |
| sortino_ratio | -0.1763 |
| max_drawdown | 0.2504 |
| cagr | -0.0782 |
| net_avg_win | 72.0874 |
| net_avg_loss | -102.2367 |
| avg_hold_time_bars | 6.6927 |
| exposure | 0.0584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
