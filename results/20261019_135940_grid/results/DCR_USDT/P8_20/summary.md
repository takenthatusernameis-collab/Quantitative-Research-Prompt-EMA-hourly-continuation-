# EMA Hourly Continuation — DCR/USDT P8_20

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1626 |
| net_profit_factor | 0.2608 |
| net_win_rate | 0.3991 |
| gross_profit_factor | 0.5498 |
| gross_win_rate | 0.4250 |
| sharpe_ratio | -13.0544 |
| sortino_ratio | -7.4501 |
| max_drawdown | 0.9999 |
| cagr | -0.9768 |
| net_avg_win | 5.4363 |
| net_avg_loss | -13.8458 |
| avg_hold_time_bars | 3.2884 |
| exposure | 0.2420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
