# EMA Hourly Continuation — 1INCH/USDT P21_34

**Symbol:** 1INCH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1235 |
| net_profit_factor | 0.3311 |
| net_win_rate | 0.4008 |
| gross_profit_factor | 0.8016 |
| gross_win_rate | 0.4445 |
| sharpe_ratio | -12.1245 |
| sortino_ratio | -6.1107 |
| max_drawdown | 0.9996 |
| cagr | -0.9539 |
| net_avg_win | 9.9961 |
| net_avg_loss | -20.1941 |
| avg_hold_time_bars | 2.5215 |
| exposure | 0.1415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
