# EMA Hourly Continuation — RLC/USDT P21_34

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.6477 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9716 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -2.7953 |
| sortino_ratio | -0.7962 |
| max_drawdown | 0.6076 |
| cagr | -0.3059 |
| net_avg_win | 56.8753 |
| net_avg_loss | -85.1796 |
| avg_hold_time_bars | 5.3299 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
