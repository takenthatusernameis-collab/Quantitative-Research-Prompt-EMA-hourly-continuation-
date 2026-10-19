# EMA Hourly Continuation — KMNO/USDT P55_89

**Symbol:** KMNO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.5525 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9900 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -4.1873 |
| sortino_ratio | -1.4094 |
| max_drawdown | 0.8174 |
| cagr | -0.4953 |
| net_avg_win | 36.7458 |
| net_avg_loss | -63.2792 |
| avg_hold_time_bars | 5.2740 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
