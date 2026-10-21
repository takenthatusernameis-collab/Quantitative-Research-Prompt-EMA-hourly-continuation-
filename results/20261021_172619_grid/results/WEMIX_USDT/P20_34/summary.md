# EMA Hourly Continuation — WEMIX/USDT P20_34

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.4637 |
| net_win_rate | 0.3803 |
| gross_profit_factor | 0.6404 |
| gross_win_rate | 0.3803 |
| sharpe_ratio | -3.8582 |
| sortino_ratio | -0.8332 |
| max_drawdown | 0.6367 |
| cagr | -0.3246 |
| net_avg_win | 60.8759 |
| net_avg_loss | -80.5889 |
| avg_hold_time_bars | 9.1154 |
| exposure | 0.0970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
