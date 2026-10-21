# EMA Hourly Continuation — IOST/USDT P20_34

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6007 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9597 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -3.6612 |
| sortino_ratio | -1.1402 |
| max_drawdown | 0.7343 |
| cagr | -0.4078 |
| net_avg_win | 48.7127 |
| net_avg_loss | -75.7277 |
| avg_hold_time_bars | 5.1132 |
| exposure | 0.1088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
