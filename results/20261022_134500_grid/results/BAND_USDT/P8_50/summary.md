# EMA Hourly Continuation — BAND/USDT P8_50

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 952 |
| net_profit_factor | 0.6478 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 1.0417 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -4.8566 |
| sortino_ratio | -2.1072 |
| max_drawdown | 0.9234 |
| cagr | -0.6366 |
| net_avg_win | 37.0420 |
| net_avg_loss | -53.0101 |
| avg_hold_time_bars | 10.9979 |
| exposure | 0.4738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
