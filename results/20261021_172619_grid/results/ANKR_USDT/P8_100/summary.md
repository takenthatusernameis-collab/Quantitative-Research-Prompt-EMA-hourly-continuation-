# EMA Hourly Continuation — ANKR/USDT P8_100

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.8137 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0246 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.4589 |
| sortino_ratio | -0.4473 |
| max_drawdown | 0.4336 |
| cagr | -0.1884 |
| net_avg_win | 76.4902 |
| net_avg_loss | -96.4827 |
| avg_hold_time_bars | 33.4891 |
| exposure | 0.7002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
