# EMA Hourly Continuation — PHA/USDT P20_200

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6247 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8632 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -3.1614 |
| sortino_ratio | -0.9597 |
| max_drawdown | 0.6891 |
| cagr | -0.3654 |
| net_avg_win | 53.1966 |
| net_avg_loss | -71.6964 |
| avg_hold_time_bars | 27.9828 |
| exposure | 0.5927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
