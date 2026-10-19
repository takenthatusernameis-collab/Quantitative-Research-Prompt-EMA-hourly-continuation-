# EMA Hourly Continuation — FLOKI/USDT P89_100

**Symbol:** FLOKI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.3130 |
| net_win_rate | 0.4154 |
| gross_profit_factor | 0.7887 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -8.2340 |
| sortino_ratio | -2.8428 |
| max_drawdown | 0.9770 |
| cagr | -0.7761 |
| net_avg_win | 18.3093 |
| net_avg_loss | -41.5668 |
| avg_hold_time_bars | 2.2803 |
| exposure | 0.0606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
