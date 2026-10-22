# EMA Hourly Continuation — TRAC/USDT P12_34

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.4639 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.8376 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -7.7290 |
| sortino_ratio | -3.3472 |
| max_drawdown | 0.9860 |
| cagr | -0.8149 |
| net_avg_win | 20.4473 |
| net_avg_loss | -33.6049 |
| avg_hold_time_bars | 6.1805 |
| exposure | 0.2708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
