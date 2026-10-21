# EMA Hourly Continuation — STRK/USDT P8_20

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.7928 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0370 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -1.4727 |
| sortino_ratio | -0.4701 |
| max_drawdown | 0.4750 |
| cagr | -0.1950 |
| net_avg_win | 63.4944 |
| net_avg_loss | -84.7852 |
| avg_hold_time_bars | 5.2175 |
| exposure | 0.1167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
