# EMA Hourly Continuation — TWT/USDT P12_144

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.5895 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9339 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -3.6207 |
| sortino_ratio | -1.2071 |
| max_drawdown | 0.7937 |
| cagr | -0.4455 |
| net_avg_win | 40.1962 |
| net_avg_loss | -64.2296 |
| avg_hold_time_bars | 25.2882 |
| exposure | 0.6540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
