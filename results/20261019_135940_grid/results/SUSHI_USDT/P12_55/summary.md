# EMA Hourly Continuation — SUSHI/USDT P12_55

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.5399 |
| net_win_rate | 0.4383 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -6.9991 |
| sortino_ratio | -3.0668 |
| max_drawdown | 0.9781 |
| cagr | -0.7800 |
| net_avg_win | 26.5061 |
| net_avg_loss | -38.3023 |
| avg_hold_time_bars | 8.8472 |
| exposure | 0.3955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
