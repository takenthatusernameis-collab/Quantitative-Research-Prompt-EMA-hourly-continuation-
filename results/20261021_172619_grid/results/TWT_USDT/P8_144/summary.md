# EMA Hourly Continuation — TWT/USDT P8_144

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.8020 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -1.2873 |
| sortino_ratio | -0.3721 |
| max_drawdown | 0.4199 |
| cagr | -0.1588 |
| net_avg_win | 68.9039 |
| net_avg_loss | -88.9256 |
| avg_hold_time_bars | 40.1990 |
| exposure | 0.7437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
