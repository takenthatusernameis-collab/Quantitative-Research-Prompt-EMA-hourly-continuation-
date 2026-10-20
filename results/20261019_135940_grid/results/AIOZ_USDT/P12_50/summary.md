# EMA Hourly Continuation — AIOZ/USDT P12_50

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1212 |
| net_profit_factor | 0.6253 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.9294 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -6.7743 |
| sortino_ratio | -3.3238 |
| max_drawdown | 0.9820 |
| cagr | -0.7958 |
| net_avg_win | 29.9986 |
| net_avg_loss | -39.3306 |
| avg_hold_time_bars | 6.2228 |
| exposure | 0.3428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
