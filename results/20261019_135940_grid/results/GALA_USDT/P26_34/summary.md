# EMA Hourly Continuation — GALA/USDT P26_34

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1115 |
| net_profit_factor | 0.2663 |
| net_win_rate | 0.3865 |
| gross_profit_factor | 0.6793 |
| gross_win_rate | 0.4179 |
| sharpe_ratio | -12.1191 |
| sortino_ratio | -5.8452 |
| max_drawdown | 0.9994 |
| cagr | -0.9477 |
| net_avg_win | 8.4161 |
| net_avg_loss | -19.9142 |
| avg_hold_time_bars | 2.1300 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
