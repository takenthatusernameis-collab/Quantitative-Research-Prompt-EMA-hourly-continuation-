# EMA Hourly Continuation — STRAX/USDT P89_200

**Symbol:** STRAX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.4767 |
| net_win_rate | 0.3939 |
| gross_profit_factor | 0.6479 |
| gross_win_rate | 0.3939 |
| sharpe_ratio | -4.2114 |
| sortino_ratio | -1.0846 |
| max_drawdown | 0.7216 |
| cagr | -0.3963 |
| net_avg_win | 50.2043 |
| net_avg_loss | -68.4528 |
| avg_hold_time_bars | 13.4364 |
| exposure | 0.2027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
