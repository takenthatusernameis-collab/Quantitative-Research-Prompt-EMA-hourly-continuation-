# EMA Hourly Continuation — REZ/USDT P34_55

**Symbol:** REZ/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.8033 |
| net_win_rate | 0.5128 |
| gross_profit_factor | 1.0658 |
| gross_win_rate | 0.5128 |
| sharpe_ratio | -1.4867 |
| sortino_ratio | -0.4259 |
| max_drawdown | 0.4507 |
| cagr | -0.1783 |
| net_avg_win | 78.1964 |
| net_avg_loss | -102.4439 |
| avg_hold_time_bars | 6.3750 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
