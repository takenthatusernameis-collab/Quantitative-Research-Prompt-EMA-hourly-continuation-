# EMA Hourly Continuation — COMP/USDT P20_34

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.6074 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9298 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.9805 |
| sortino_ratio | -0.9050 |
| max_drawdown | 0.6881 |
| cagr | -0.3390 |
| net_avg_win | 45.0457 |
| net_avg_loss | -73.5000 |
| avg_hold_time_bars | 5.1951 |
| exposure | 0.1053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
