# EMA Hourly Continuation — AR/USDT P26_144

**Symbol:** AR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7764 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9138 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -1.4818 |
| sortino_ratio | -0.4049 |
| max_drawdown | 0.4372 |
| cagr | -0.1713 |
| net_avg_win | 73.8017 |
| net_avg_loss | -88.0846 |
| avg_hold_time_bars | 29.0489 |
| exposure | 0.4859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
