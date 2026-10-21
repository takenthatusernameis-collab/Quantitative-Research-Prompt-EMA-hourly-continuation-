# EMA Hourly Continuation — KMNO/USDT P20_34

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7107 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0182 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -1.9761 |
| sortino_ratio | -0.5292 |
| max_drawdown | 0.4642 |
| cagr | -0.2160 |
| net_avg_win | 64.1801 |
| net_avg_loss | -91.9039 |
| avg_hold_time_bars | 5.7347 |
| exposure | 0.0908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
