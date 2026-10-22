# EMA Hourly Continuation — XLM/USDT P8_55

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.4333 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -6.6206 |
| sortino_ratio | -3.0473 |
| max_drawdown | 0.9780 |
| cagr | -0.7780 |
| net_avg_win | 14.5062 |
| net_avg_loss | -30.4097 |
| avg_hold_time_bars | 9.8383 |
| exposure | 0.4839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
