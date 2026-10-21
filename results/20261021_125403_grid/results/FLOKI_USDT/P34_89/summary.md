# EMA Hourly Continuation — FLOKI/USDT P34_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.7907 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 0.9980 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.4892 |
| sortino_ratio | -0.4527 |
| max_drawdown | 0.4385 |
| cagr | -0.1882 |
| net_avg_win | 68.1463 |
| net_avg_loss | -87.3420 |
| avg_hold_time_bars | 12.3875 |
| exposure | 0.2528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
