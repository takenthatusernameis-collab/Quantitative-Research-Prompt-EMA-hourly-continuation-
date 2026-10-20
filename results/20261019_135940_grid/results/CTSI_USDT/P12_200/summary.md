# EMA Hourly Continuation — CTSI/USDT P12_200

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.6617 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.9191 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -2.6772 |
| sortino_ratio | -0.7433 |
| max_drawdown | 0.5933 |
| cagr | -0.2948 |
| net_avg_win | 63.1285 |
| net_avg_loss | -83.4154 |
| avg_hold_time_bars | 41.4098 |
| exposure | 0.7303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
