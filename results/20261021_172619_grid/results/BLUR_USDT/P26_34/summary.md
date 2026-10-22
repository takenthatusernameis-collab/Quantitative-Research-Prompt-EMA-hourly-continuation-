# EMA Hourly Continuation — BLUR/USDT P26_34

**Symbol:** BLUR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.5336 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.7864 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -2.9168 |
| sortino_ratio | -0.6586 |
| max_drawdown | 0.5493 |
| cagr | -0.2612 |
| net_avg_win | 54.5503 |
| net_avg_loss | -82.3730 |
| avg_hold_time_bars | 4.4343 |
| exposure | 0.0504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
