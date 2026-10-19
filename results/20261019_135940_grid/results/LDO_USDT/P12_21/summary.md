# EMA Hourly Continuation — LDO/USDT P12_21

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1523 |
| net_profit_factor | 0.2790 |
| net_win_rate | 0.3775 |
| gross_profit_factor | 0.6347 |
| gross_win_rate | 0.4084 |
| sharpe_ratio | -13.9858 |
| sortino_ratio | -7.7569 |
| max_drawdown | 1.0000 |
| cagr | -0.9820 |
| net_avg_win | 6.7293 |
| net_avg_loss | -14.6297 |
| avg_hold_time_bars | 2.0906 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
