# EMA Hourly Continuation — JASMY/USDT P21_100

**Symbol:** JASMY/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.7545 |
| net_win_rate | 0.5274 |
| gross_profit_factor | 1.1100 |
| gross_win_rate | 0.5348 |
| sharpe_ratio | -2.1390 |
| sortino_ratio | -0.7887 |
| max_drawdown | 0.6724 |
| cagr | -0.3129 |
| net_avg_win | 52.7000 |
| net_avg_loss | -77.9451 |
| avg_hold_time_bars | 12.6681 |
| exposure | 0.3887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
