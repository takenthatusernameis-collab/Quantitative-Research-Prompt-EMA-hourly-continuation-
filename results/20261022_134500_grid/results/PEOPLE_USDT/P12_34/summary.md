# EMA Hourly Continuation — PEOPLE/USDT P12_34

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1279 |
| net_profit_factor | 0.4636 |
| net_win_rate | 0.4199 |
| gross_profit_factor | 0.7460 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -8.7528 |
| sortino_ratio | -4.3830 |
| max_drawdown | 0.9954 |
| cagr | -0.8813 |
| net_avg_win | 16.0222 |
| net_avg_loss | -25.0104 |
| avg_hold_time_bars | 4.2283 |
| exposure | 0.2447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
