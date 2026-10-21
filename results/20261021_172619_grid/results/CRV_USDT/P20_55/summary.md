# EMA Hourly Continuation — CRV/USDT P20_55

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.8372 |
| net_win_rate | 0.5170 |
| gross_profit_factor | 1.0759 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -1.3195 |
| sortino_ratio | -0.4251 |
| max_drawdown | 0.4253 |
| cagr | -0.1789 |
| net_avg_win | 77.5482 |
| net_avg_loss | -99.1326 |
| avg_hold_time_bars | 7.8523 |
| exposure | 0.1788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
