# EMA Hourly Continuation — MAGIC/USDT P55_89

**Symbol:** MAGIC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.7071 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.2877 |
| sortino_ratio | -0.6369 |
| max_drawdown | 0.5355 |
| cagr | -0.2538 |
| net_avg_win | 67.5796 |
| net_avg_loss | -93.0698 |
| avg_hold_time_bars | 6.2281 |
| exposure | 0.1067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
