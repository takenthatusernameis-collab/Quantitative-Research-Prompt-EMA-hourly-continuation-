# EMA Hourly Continuation — CYBER/USDT P26_34

**Symbol:** CYBER/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.6633 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 1.0162 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -2.3009 |
| sortino_ratio | -0.5792 |
| max_drawdown | 0.4997 |
| cagr | -0.2330 |
| net_avg_win | 62.2183 |
| net_avg_loss | -94.4143 |
| avg_hold_time_bars | 6.1401 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
