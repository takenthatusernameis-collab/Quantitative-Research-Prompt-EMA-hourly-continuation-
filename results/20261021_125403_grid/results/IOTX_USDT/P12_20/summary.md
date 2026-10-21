# EMA Hourly Continuation — IOTX/USDT P12_20

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7810 |
| net_win_rate | 0.5382 |
| gross_profit_factor | 1.1586 |
| gross_win_rate | 0.5382 |
| sharpe_ratio | -1.3842 |
| sortino_ratio | -0.3700 |
| max_drawdown | 0.3624 |
| cagr | -0.1552 |
| net_avg_win | 67.3053 |
| net_avg_loss | -100.4457 |
| avg_hold_time_bars | 5.0735 |
| exposure | 0.0784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
