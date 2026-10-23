# EMA Hourly Continuation — FIDA/USDT P8_26

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1411 |
| net_profit_factor | 0.4383 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7744 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -8.5511 |
| sortino_ratio | -4.5194 |
| max_drawdown | 0.9960 |
| cagr | -0.8877 |
| net_avg_win | 12.3972 |
| net_avg_loss | -22.6184 |
| avg_hold_time_bars | 4.7186 |
| exposure | 0.3013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
