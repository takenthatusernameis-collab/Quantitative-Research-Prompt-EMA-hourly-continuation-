# EMA Hourly Continuation — CETUS/USDT P20_26

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1202 |
| net_profit_factor | 0.3477 |
| net_win_rate | 0.3869 |
| gross_profit_factor | 0.8831 |
| gross_win_rate | 0.4243 |
| sharpe_ratio | -12.6323 |
| sortino_ratio | -6.2339 |
| max_drawdown | 0.9998 |
| cagr | -0.9627 |
| net_avg_win | 11.4618 |
| net_avg_loss | -20.7968 |
| avg_hold_time_bars | 2.1830 |
| exposure | 0.1187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
