# EMA Hourly Continuation — MOVR/USDT P20_34

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6942 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9870 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -2.3757 |
| sortino_ratio | -0.7114 |
| max_drawdown | 0.5987 |
| cagr | -0.2778 |
| net_avg_win | 58.6885 |
| net_avg_loss | -83.3840 |
| avg_hold_time_bars | 4.8322 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
