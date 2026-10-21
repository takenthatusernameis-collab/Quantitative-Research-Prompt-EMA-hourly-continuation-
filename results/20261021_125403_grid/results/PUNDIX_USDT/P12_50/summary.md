# EMA Hourly Continuation — PUNDIX/USDT P12_50

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.6785 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.9438 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.6132 |
| sortino_ratio | -1.3516 |
| max_drawdown | 0.7945 |
| cagr | -0.4619 |
| net_avg_win | 50.7683 |
| net_avg_loss | -68.5561 |
| avg_hold_time_bars | 11.1356 |
| exposure | 0.3472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
