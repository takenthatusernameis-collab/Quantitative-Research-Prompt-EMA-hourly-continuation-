# EMA Hourly Continuation — ARB/USDT P26_200

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.7707 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0722 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -1.6094 |
| sortino_ratio | -0.4199 |
| max_drawdown | 0.4511 |
| cagr | -0.1828 |
| net_avg_win | 76.3504 |
| net_avg_loss | -103.8175 |
| avg_hold_time_bars | 38.4766 |
| exposure | 0.5981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
