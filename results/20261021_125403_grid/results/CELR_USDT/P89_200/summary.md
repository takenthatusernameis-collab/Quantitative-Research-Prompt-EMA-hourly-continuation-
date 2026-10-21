# EMA Hourly Continuation — CELR/USDT P89_200

**Symbol:** CELR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6873 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -1.9498 |
| sortino_ratio | -0.4895 |
| max_drawdown | 0.4745 |
| cagr | -0.2022 |
| net_avg_win | 64.9686 |
| net_avg_loss | -84.2112 |
| avg_hold_time_bars | 14.8654 |
| exposure | 0.2099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
