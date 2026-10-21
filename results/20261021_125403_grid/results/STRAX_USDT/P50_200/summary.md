# EMA Hourly Continuation — STRAX/USDT P50_200

**Symbol:** STRAX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.5873 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.7641 |
| gross_win_rate | 0.4301 |
| sharpe_ratio | -3.2936 |
| sortino_ratio | -0.8927 |
| max_drawdown | 0.6488 |
| cagr | -0.3378 |
| net_avg_win | 58.2412 |
| net_avg_loss | -74.8588 |
| avg_hold_time_bars | 21.4247 |
| exposure | 0.3575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
