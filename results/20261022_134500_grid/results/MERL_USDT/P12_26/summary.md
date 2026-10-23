# EMA Hourly Continuation — MERL/USDT P12_26

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1402 |
| net_profit_factor | 0.4823 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.7550 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -8.8611 |
| sortino_ratio | -4.6721 |
| max_drawdown | 0.9967 |
| cagr | -0.8975 |
| net_avg_win | 15.3986 |
| net_avg_loss | -24.0951 |
| avg_hold_time_bars | 3.2361 |
| exposure | 0.2068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
