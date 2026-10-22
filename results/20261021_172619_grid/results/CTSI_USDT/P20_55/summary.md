# EMA Hourly Continuation — CTSI/USDT P20_55

**Symbol:** CTSI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.6821 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.9208 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -3.8070 |
| sortino_ratio | -1.3791 |
| max_drawdown | 0.8068 |
| cagr | -0.4693 |
| net_avg_win | 57.7131 |
| net_avg_loss | -71.5587 |
| avg_hold_time_bars | 7.9659 |
| exposure | 0.2339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
