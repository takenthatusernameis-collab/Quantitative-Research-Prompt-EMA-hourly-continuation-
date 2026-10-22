# EMA Hourly Continuation — BICO/USDT P26_200

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.7392 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.8528 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -1.5514 |
| sortino_ratio | -0.3728 |
| max_drawdown | 0.4015 |
| cagr | -0.1587 |
| net_avg_win | 75.0344 |
| net_avg_loss | -87.6627 |
| avg_hold_time_bars | 45.3693 |
| exposure | 0.5919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
