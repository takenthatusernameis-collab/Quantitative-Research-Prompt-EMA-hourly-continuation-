# EMA Hourly Continuation — LUNA/USDT P8_200

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.5746 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8963 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -3.9432 |
| sortino_ratio | -1.2018 |
| max_drawdown | 0.7766 |
| cagr | -0.4433 |
| net_avg_win | 48.1672 |
| net_avg_loss | -69.9116 |
| avg_hold_time_bars | 35.2674 |
| exposure | 0.7615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
