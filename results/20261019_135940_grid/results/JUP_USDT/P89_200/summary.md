# EMA Hourly Continuation — JUP/USDT P89_200

**Symbol:** JUP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.5468 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8136 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -3.4684 |
| sortino_ratio | -0.9692 |
| max_drawdown | 0.7003 |
| cagr | -0.3683 |
| net_avg_win | 46.6594 |
| net_avg_loss | -70.2475 |
| avg_hold_time_bars | 9.6888 |
| exposure | 0.1726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
