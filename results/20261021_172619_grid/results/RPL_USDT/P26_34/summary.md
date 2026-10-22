# EMA Hourly Continuation — RPL/USDT P26_34

**Symbol:** RPL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.9341 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -3.3350 |
| sortino_ratio | -0.9322 |
| max_drawdown | 0.6612 |
| cagr | -0.3489 |
| net_avg_win | 61.1366 |
| net_avg_loss | -85.3402 |
| avg_hold_time_bars | 5.9661 |
| exposure | 0.1034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
