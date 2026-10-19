# EMA Hourly Continuation — LDO/USDT P8_21

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1756 |
| net_profit_factor | 0.3398 |
| net_win_rate | 0.4077 |
| gross_profit_factor | 0.6893 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -12.5349 |
| sortino_ratio | -7.3905 |
| max_drawdown | 0.9999 |
| cagr | -0.9760 |
| net_avg_win | 7.1884 |
| net_avg_loss | -14.5635 |
| avg_hold_time_bars | 2.7005 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
