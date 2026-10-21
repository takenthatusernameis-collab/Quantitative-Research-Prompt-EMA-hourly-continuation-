# EMA Hourly Continuation — DCR/USDT P89_100

**Symbol:** DCR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 188 |
| net_profit_factor | 0.4832 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.7817 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -2.9019 |
| sortino_ratio | -0.5697 |
| max_drawdown | 0.4914 |
| cagr | -0.2327 |
| net_avg_win | 54.2356 |
| net_avg_loss | -90.6664 |
| avg_hold_time_bars | 5.4947 |
| exposure | 0.0467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
