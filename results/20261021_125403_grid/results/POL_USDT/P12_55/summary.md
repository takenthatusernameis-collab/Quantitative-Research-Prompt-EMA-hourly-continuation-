# EMA Hourly Continuation — POL/USDT P12_55

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.5880 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.7790 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -3.5140 |
| sortino_ratio | -1.1786 |
| max_drawdown | 0.7586 |
| cagr | -0.4191 |
| net_avg_win | 42.3215 |
| net_avg_loss | -59.2356 |
| avg_hold_time_bars | 15.2932 |
| exposure | 0.3865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
