# EMA Hourly Continuation — FET/USDT P34_50

**Symbol:** FET/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.2931 |
| net_win_rate | 0.4146 |
| gross_profit_factor | 0.5897 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -9.2129 |
| sortino_ratio | -3.9178 |
| max_drawdown | 0.9932 |
| cagr | -0.8624 |
| net_avg_win | 11.0097 |
| net_avg_loss | -26.6080 |
| avg_hold_time_bars | 2.4468 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
