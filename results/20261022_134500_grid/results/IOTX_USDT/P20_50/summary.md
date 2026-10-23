# EMA Hourly Continuation — IOTX/USDT P20_50

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.5444 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.9866 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -7.2024 |
| sortino_ratio | -3.2325 |
| max_drawdown | 0.9821 |
| cagr | -0.7958 |
| net_avg_win | 25.0611 |
| net_avg_loss | -39.3848 |
| avg_hold_time_bars | 4.3537 |
| exposure | 0.2009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
