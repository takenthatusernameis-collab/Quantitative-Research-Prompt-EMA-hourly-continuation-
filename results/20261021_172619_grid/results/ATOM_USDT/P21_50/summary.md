# EMA Hourly Continuation — ATOM/USDT P21_50

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.6740 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -2.5639 |
| sortino_ratio | -0.7879 |
| max_drawdown | 0.6100 |
| cagr | -0.3027 |
| net_avg_win | 54.9795 |
| net_avg_loss | -77.7499 |
| avg_hold_time_bars | 7.7560 |
| exposure | 0.1618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
