# EMA Hourly Continuation — ATH/USDT P20_26

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1102 |
| net_profit_factor | 0.3371 |
| net_win_rate | 0.3893 |
| gross_profit_factor | 0.7875 |
| gross_win_rate | 0.4256 |
| sharpe_ratio | -12.4250 |
| sortino_ratio | -6.0868 |
| max_drawdown | 0.9995 |
| cagr | -0.9595 |
| net_avg_win | 11.8459 |
| net_avg_loss | -22.4021 |
| avg_hold_time_bars | 1.9111 |
| exposure | 0.1021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
