# EMA Hourly Continuation — CARV/USDT P34_55

**Symbol:** CARV/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.4277 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.8660 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -6.7579 |
| sortino_ratio | -2.5851 |
| max_drawdown | 0.9243 |
| cagr | -0.7168 |
| net_avg_win | 26.2186 |
| net_avg_loss | -49.6049 |
| avg_hold_time_bars | 4.0629 |
| exposure | 0.1344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
