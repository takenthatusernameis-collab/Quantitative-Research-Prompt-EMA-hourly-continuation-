# EMA Hourly Continuation — LDO/USDT P8_20

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7102 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9464 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -2.4004 |
| sortino_ratio | -0.7990 |
| max_drawdown | 0.6095 |
| cagr | -0.3065 |
| net_avg_win | 55.5810 |
| net_avg_loss | -75.4180 |
| avg_hold_time_bars | 4.7500 |
| exposure | 0.1166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
