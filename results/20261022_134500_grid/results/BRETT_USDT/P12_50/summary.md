# EMA Hourly Continuation — BRETT/USDT P12_50

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.6135 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8819 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -5.5974 |
| sortino_ratio | -2.5531 |
| max_drawdown | 0.9482 |
| cagr | -0.7129 |
| net_avg_win | 32.5034 |
| net_avg_loss | -44.6832 |
| avg_hold_time_bars | 7.2342 |
| exposure | 0.3523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
