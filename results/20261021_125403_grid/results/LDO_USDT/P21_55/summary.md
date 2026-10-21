# EMA Hourly Continuation — LDO/USDT P21_55

**Symbol:** LDO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7227 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9147 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.3489 |
| sortino_ratio | -0.7630 |
| max_drawdown | 0.5922 |
| cagr | -0.2954 |
| net_avg_win | 61.4554 |
| net_avg_loss | -78.1108 |
| avg_hold_time_bars | 7.9093 |
| exposure | 0.1862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
