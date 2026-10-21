# EMA Hourly Continuation — QNT/USDT P20_55

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7248 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -2.2565 |
| sortino_ratio | -0.7544 |
| max_drawdown | 0.6016 |
| cagr | -0.2913 |
| net_avg_win | 55.4447 |
| net_avg_loss | -79.3820 |
| avg_hold_time_bars | 7.1667 |
| exposure | 0.1759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
