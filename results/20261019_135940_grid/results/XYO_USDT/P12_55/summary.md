# EMA Hourly Continuation — XYO/USDT P12_55

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.4314 |
| net_win_rate | 0.4056 |
| gross_profit_factor | 0.7671 |
| gross_win_rate | 0.4230 |
| sharpe_ratio | -9.5887 |
| sortino_ratio | -4.5722 |
| max_drawdown | 0.9968 |
| cagr | -0.8956 |
| net_avg_win | 16.2253 |
| net_avg_loss | -25.6626 |
| avg_hold_time_bars | 7.3829 |
| exposure | 0.3839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
