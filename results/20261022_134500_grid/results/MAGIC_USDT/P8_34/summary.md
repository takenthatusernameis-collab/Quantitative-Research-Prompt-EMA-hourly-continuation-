# EMA Hourly Continuation — MAGIC/USDT P8_34

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1268 |
| net_profit_factor | 0.6258 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 1.0470 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -6.6813 |
| sortino_ratio | -3.3568 |
| max_drawdown | 0.9827 |
| cagr | -0.7992 |
| net_avg_win | 27.6123 |
| net_avg_loss | -39.0072 |
| avg_hold_time_bars | 6.3013 |
| exposure | 0.3632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
