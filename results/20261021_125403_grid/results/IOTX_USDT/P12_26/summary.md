# EMA Hourly Continuation — IOTX/USDT P12_26

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.7256 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0455 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -2.1322 |
| sortino_ratio | -0.6982 |
| max_drawdown | 0.5707 |
| cagr | -0.2729 |
| net_avg_win | 54.5417 |
| net_avg_loss | -80.6047 |
| avg_hold_time_bars | 5.2713 |
| exposure | 0.1236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
