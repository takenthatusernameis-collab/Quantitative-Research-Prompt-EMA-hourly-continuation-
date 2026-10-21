# EMA Hourly Continuation — LDO/USDT P8_12

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.6626 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9071 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -2.0080 |
| sortino_ratio | -0.4760 |
| max_drawdown | 0.4250 |
| cagr | -0.1958 |
| net_avg_win | 62.6912 |
| net_avg_loss | -87.9513 |
| avg_hold_time_bars | 3.7409 |
| exposure | 0.0466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
