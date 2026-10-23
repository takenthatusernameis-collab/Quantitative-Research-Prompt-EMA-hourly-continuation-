# EMA Hourly Continuation — NYM/USDT P20_26

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1083 |
| net_profit_factor | 0.0971 |
| net_win_rate | 0.2207 |
| gross_profit_factor | 0.4529 |
| gross_win_rate | 0.3001 |
| sharpe_ratio | -19.5632 |
| sortino_ratio | -10.2831 |
| max_drawdown | 1.0000 |
| cagr | -0.9973 |
| net_avg_win | 4.5009 |
| net_avg_loss | -13.1229 |
| avg_hold_time_bars | 3.1404 |
| exposure | 0.1546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
