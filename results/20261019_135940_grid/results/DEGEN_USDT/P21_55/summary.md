# EMA Hourly Continuation — DEGEN/USDT P21_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 887 |
| net_profit_factor | 0.6081 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8712 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -5.3858 |
| sortino_ratio | -2.2649 |
| max_drawdown | 0.9352 |
| cagr | -0.6596 |
| net_avg_win | 36.0031 |
| net_avg_loss | -49.0773 |
| avg_hold_time_bars | 5.8388 |
| exposure | 0.2358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
