# EMA Hourly Continuation — MINA/USDT P8_12

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7422 |
| net_win_rate | 0.5299 |
| gross_profit_factor | 1.1268 |
| gross_win_rate | 0.5299 |
| sharpe_ratio | -1.8332 |
| sortino_ratio | -0.5080 |
| max_drawdown | 0.4937 |
| cagr | -0.2070 |
| net_avg_win | 65.1921 |
| net_avg_loss | -99.0029 |
| avg_hold_time_bars | 4.5299 |
| exposure | 0.0758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
