# EMA Hourly Continuation — FLOKI/USDT P20_21

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1317 |
| net_profit_factor | 0.1468 |
| net_win_rate | 0.2787 |
| gross_profit_factor | 0.4797 |
| gross_win_rate | 0.3333 |
| sharpe_ratio | -19.2265 |
| sortino_ratio | -10.6504 |
| max_drawdown | 1.0000 |
| cagr | -0.9976 |
| net_avg_win | 4.6882 |
| net_avg_loss | -12.3375 |
| avg_hold_time_bars | 1.6287 |
| exposure | 0.0975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
