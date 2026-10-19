# EMA Hourly Continuation — JST/USDT P21_26

**Symbol:** JST/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.0445 |
| net_win_rate | 0.2620 |
| gross_profit_factor | 0.5472 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -16.6050 |
| sortino_ratio | -8.0817 |
| max_drawdown | 1.0000 |
| cagr | -0.9886 |
| net_avg_win | 1.8535 |
| net_avg_loss | -14.8021 |
| avg_hold_time_bars | 2.4864 |
| exposure | 0.1078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
