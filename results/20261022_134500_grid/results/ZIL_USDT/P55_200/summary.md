# EMA Hourly Continuation — ZIL/USDT P55_200

**Symbol:** ZIL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6386 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 1.0154 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -2.5958 |
| sortino_ratio | -0.7127 |
| max_drawdown | 0.5870 |
| cagr | -0.2897 |
| net_avg_win | 53.8914 |
| net_avg_loss | -82.6426 |
| avg_hold_time_bars | 21.5105 |
| exposure | 0.3735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
