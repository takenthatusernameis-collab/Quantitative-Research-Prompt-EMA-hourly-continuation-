# EMA Hourly Continuation — ARB/USDT P26_34

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1017 |
| net_profit_factor | 0.2053 |
| net_win_rate | 0.4081 |
| gross_profit_factor | 0.6665 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -11.3448 |
| sortino_ratio | -5.1706 |
| max_drawdown | 0.9990 |
| cagr | -0.9346 |
| net_avg_win | 6.2166 |
| net_avg_loss | -20.8792 |
| avg_hold_time_bars | 2.1042 |
| exposure | 0.0973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
