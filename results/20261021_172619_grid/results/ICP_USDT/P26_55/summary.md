# EMA Hourly Continuation — ICP/USDT P26_55

**Symbol:** ICP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7146 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9571 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -2.1837 |
| sortino_ratio | -0.6330 |
| max_drawdown | 0.5239 |
| cagr | -0.2521 |
| net_avg_win | 64.8309 |
| net_avg_loss | -86.4041 |
| avg_hold_time_bars | 7.1366 |
| exposure | 0.1330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
