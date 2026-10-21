# EMA Hourly Continuation — IO/USDT P20_55

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.7877 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9577 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -1.6831 |
| sortino_ratio | -0.5311 |
| max_drawdown | 0.4490 |
| cagr | -0.2176 |
| net_avg_win | 72.7712 |
| net_avg_loss | -88.4340 |
| avg_hold_time_bars | 9.0633 |
| exposure | 0.2010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
