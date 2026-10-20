# EMA Hourly Continuation — POPCAT/USDT P55_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.6342 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8339 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -3.3249 |
| sortino_ratio | -1.0591 |
| max_drawdown | 0.6667 |
| cagr | -0.3934 |
| net_avg_win | 56.9634 |
| net_avg_loss | -75.5429 |
| avg_hold_time_bars | 12.7068 |
| exposure | 0.2954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
