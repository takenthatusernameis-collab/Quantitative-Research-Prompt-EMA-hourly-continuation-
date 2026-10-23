# EMA Hourly Continuation — ARKM/USDT P55_100

**Symbol:** ARKM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.5490 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.8903 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -4.5049 |
| sortino_ratio | -1.6166 |
| max_drawdown | 0.8596 |
| cagr | -0.5409 |
| net_avg_win | 33.8105 |
| net_avg_loss | -56.3066 |
| avg_hold_time_bars | 4.6754 |
| exposure | 0.1375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
