# EMA Hourly Continuation — LUNC/USDT P55_144

**Symbol:** LUNC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.5529 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9327 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -4.1179 |
| sortino_ratio | -1.3539 |
| max_drawdown | 0.8089 |
| cagr | -0.4741 |
| net_avg_win | 38.6801 |
| net_avg_loss | -63.9671 |
| avg_hold_time_bars | 10.6791 |
| exposure | 0.2602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
