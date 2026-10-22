# EMA Hourly Continuation — LDO/USDT P21_50

**Symbol:** LDO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.4568 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.8234 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -7.8151 |
| sortino_ratio | -3.5547 |
| max_drawdown | 0.9881 |
| cagr | -0.8275 |
| net_avg_win | 17.9018 |
| net_avg_loss | -31.0861 |
| avg_hold_time_bars | 4.1449 |
| exposure | 0.1976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
