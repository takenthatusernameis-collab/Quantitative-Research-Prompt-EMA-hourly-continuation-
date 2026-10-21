# EMA Hourly Continuation — INJ/USDT P8_21

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.7820 |
| net_win_rate | 0.5120 |
| gross_profit_factor | 1.0259 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -1.6019 |
| sortino_ratio | -0.5141 |
| max_drawdown | 0.5081 |
| cagr | -0.2108 |
| net_avg_win | 63.0476 |
| net_avg_loss | -84.6028 |
| avg_hold_time_bars | 6.1426 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
