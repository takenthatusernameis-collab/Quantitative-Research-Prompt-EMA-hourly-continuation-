# EMA Hourly Continuation — ONDO/USDT P8_34

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1386 |
| net_profit_factor | 0.5622 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9162 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -6.7889 |
| sortino_ratio | -3.5347 |
| max_drawdown | 0.9874 |
| cagr | -0.8235 |
| net_avg_win | 19.0664 |
| net_avg_loss | -31.2771 |
| avg_hold_time_bars | 5.1869 |
| exposure | 0.3268 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
