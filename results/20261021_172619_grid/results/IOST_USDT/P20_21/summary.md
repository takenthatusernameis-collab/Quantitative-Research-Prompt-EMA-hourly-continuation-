# EMA Hourly Continuation — IOST/USDT P20_21

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.5261 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.9132 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -3.3497 |
| sortino_ratio | -0.7696 |
| max_drawdown | 0.5932 |
| cagr | -0.2983 |
| net_avg_win | 55.4285 |
| net_avg_loss | -92.0974 |
| avg_hold_time_bars | 4.6680 |
| exposure | 0.0537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
