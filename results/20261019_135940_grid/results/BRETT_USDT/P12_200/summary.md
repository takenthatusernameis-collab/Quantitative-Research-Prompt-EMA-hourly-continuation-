# EMA Hourly Continuation — BRETT/USDT P12_200

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.7976 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9874 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.1924 |
| sortino_ratio | -0.2920 |
| max_drawdown | 0.2928 |
| cagr | -0.1299 |
| net_avg_win | 78.5881 |
| net_avg_loss | -97.8332 |
| avg_hold_time_bars | 57.8693 |
| exposure | 0.7880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
