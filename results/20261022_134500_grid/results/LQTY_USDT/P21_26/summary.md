# EMA Hourly Continuation — LQTY/USDT P21_26

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1228 |
| net_profit_factor | 0.2735 |
| net_win_rate | 0.4039 |
| gross_profit_factor | 0.8351 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -12.7640 |
| sortino_ratio | -6.4058 |
| max_drawdown | 0.9998 |
| cagr | -0.9641 |
| net_avg_win | 7.5900 |
| net_avg_loss | -18.8010 |
| avg_hold_time_bars | 2.2386 |
| exposure | 0.1244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
