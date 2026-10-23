# EMA Hourly Continuation — MLK/USDT P12_20

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1786 |
| net_profit_factor | 0.1505 |
| net_win_rate | 0.2094 |
| gross_profit_factor | 0.5425 |
| gross_win_rate | 0.2441 |
| sharpe_ratio | -23.9665 |
| sortino_ratio | -15.1282 |
| max_drawdown | 1.0000 |
| cagr | -0.9997 |
| net_avg_win | 4.7355 |
| net_avg_loss | -8.3364 |
| avg_hold_time_bars | 2.4496 |
| exposure | 0.1980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
