# EMA Hourly Continuation — AERO/USDT P20_21

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1111 |
| net_profit_factor | 0.1171 |
| net_win_rate | 0.2934 |
| gross_profit_factor | 0.3933 |
| gross_win_rate | 0.3582 |
| sharpe_ratio | -17.0965 |
| sortino_ratio | -8.6487 |
| max_drawdown | 1.0000 |
| cagr | -0.9929 |
| net_avg_win | 4.0666 |
| net_avg_loss | -14.4276 |
| avg_hold_time_bars | 1.5860 |
| exposure | 0.0801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
