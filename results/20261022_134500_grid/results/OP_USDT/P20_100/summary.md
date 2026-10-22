# EMA Hourly Continuation — OP/USDT P20_100

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.6095 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.9112 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -3.9207 |
| sortino_ratio | -1.3596 |
| max_drawdown | 0.8124 |
| cagr | -0.4765 |
| net_avg_win | 44.2989 |
| net_avg_loss | -63.6780 |
| avg_hold_time_bars | 16.5396 |
| exposure | 0.4556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
