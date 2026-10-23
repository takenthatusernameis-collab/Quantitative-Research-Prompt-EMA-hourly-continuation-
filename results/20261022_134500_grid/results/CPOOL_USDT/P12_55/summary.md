# EMA Hourly Continuation — CPOOL/USDT P12_55

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.6026 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8394 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -5.7426 |
| sortino_ratio | -2.5887 |
| max_drawdown | 0.9601 |
| cagr | -0.7208 |
| net_avg_win | 30.3139 |
| net_avg_loss | -42.4336 |
| avg_hold_time_bars | 7.5081 |
| exposure | 0.3580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
