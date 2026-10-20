# EMA Hourly Continuation — BRETT/USDT P26_34

**Symbol:** BRETT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.3132 |
| net_win_rate | 0.3936 |
| gross_profit_factor | 0.6353 |
| gross_win_rate | 0.4106 |
| sharpe_ratio | -10.6858 |
| sortino_ratio | -4.9341 |
| max_drawdown | 0.9975 |
| cagr | -0.9201 |
| net_avg_win | 11.5446 |
| net_avg_loss | -23.9269 |
| avg_hold_time_bars | 2.1948 |
| exposure | 0.1057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
