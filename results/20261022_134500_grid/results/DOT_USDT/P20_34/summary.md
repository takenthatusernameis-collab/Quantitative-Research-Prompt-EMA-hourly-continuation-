# EMA Hourly Continuation — DOT/USDT P20_34

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.3203 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.8345 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -10.9080 |
| sortino_ratio | -5.2010 |
| max_drawdown | 0.9988 |
| cagr | -0.9292 |
| net_avg_win | 10.0156 |
| net_avg_loss | -22.6416 |
| avg_hold_time_bars | 2.6372 |
| exposure | 0.1341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
