# EMA Hourly Continuation — LUNC/USDT P20_26

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 164 |
| net_profit_factor | 0.5872 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8468 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -2.1435 |
| sortino_ratio | -0.3930 |
| max_drawdown | 0.3865 |
| cagr | -0.1652 |
| net_avg_win | 69.1388 |
| net_avg_loss | -99.2286 |
| avg_hold_time_bars | 4.2134 |
| exposure | 0.0314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
