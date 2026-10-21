# EMA Hourly Continuation — POLYX/USDT P34_200

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.7857 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9758 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.3510 |
| sortino_ratio | -0.3482 |
| max_drawdown | 0.3788 |
| cagr | -0.1493 |
| net_avg_win | 75.5491 |
| net_avg_loss | -94.9784 |
| avg_hold_time_bars | 32.8282 |
| exposure | 0.4865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
