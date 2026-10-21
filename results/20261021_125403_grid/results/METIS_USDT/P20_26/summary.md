# EMA Hourly Continuation — METIS/USDT P20_26

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.6408 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -2.2101 |
| sortino_ratio | -0.4736 |
| max_drawdown | 0.4457 |
| cagr | -0.1957 |
| net_avg_win | 70.8920 |
| net_avg_loss | -99.3869 |
| avg_hold_time_bars | 4.3973 |
| exposure | 0.0448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
