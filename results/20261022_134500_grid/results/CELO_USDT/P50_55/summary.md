# EMA Hourly Continuation — CELO/USDT P50_55

**Symbol:** CELO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 791 |
| net_profit_factor | 0.2142 |
| net_win_rate | 0.3679 |
| gross_profit_factor | 0.6564 |
| gross_win_rate | 0.4324 |
| sharpe_ratio | -11.4974 |
| sortino_ratio | -4.7002 |
| max_drawdown | 0.9984 |
| cagr | -0.9208 |
| net_avg_win | 9.3541 |
| net_avg_loss | -25.4108 |
| avg_hold_time_bars | 2.2731 |
| exposure | 0.0814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
