# EMA Hourly Continuation — LTC/USDT P8_200

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.3641 |
| net_win_rate | 0.4141 |
| gross_profit_factor | 0.7373 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -5.7094 |
| sortino_ratio | -1.6935 |
| max_drawdown | 0.8907 |
| cagr | -0.5796 |
| net_avg_win | 27.0037 |
| net_avg_loss | -52.4140 |
| avg_hold_time_bars | 37.0859 |
| exposure | 0.7653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
