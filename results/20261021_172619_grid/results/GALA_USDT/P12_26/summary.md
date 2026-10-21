# EMA Hourly Continuation — GALA/USDT P12_26

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6627 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -2.6882 |
| sortino_ratio | -0.7899 |
| max_drawdown | 0.6081 |
| cagr | -0.3041 |
| net_avg_win | 59.0166 |
| net_avg_loss | -79.1142 |
| avg_hold_time_bars | 5.1915 |
| exposure | 0.0998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
