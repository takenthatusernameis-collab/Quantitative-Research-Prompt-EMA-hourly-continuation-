# EMA Hourly Continuation — RIO/USDT P89_100

**Symbol:** RIO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 85 |
| net_profit_factor | 0.3830 |
| net_win_rate | 0.3176 |
| gross_profit_factor | 0.4629 |
| gross_win_rate | 0.3176 |
| sharpe_ratio | -2.6334 |
| sortino_ratio | -0.3410 |
| max_drawdown | 0.3258 |
| cagr | -0.1466 |
| net_avg_win | 74.8868 |
| net_avg_loss | -91.0265 |
| avg_hold_time_bars | 5.6824 |
| exposure | 0.0222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
