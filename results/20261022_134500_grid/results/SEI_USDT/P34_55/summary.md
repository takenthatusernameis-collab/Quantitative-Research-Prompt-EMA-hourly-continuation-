# EMA Hourly Continuation — SEI/USDT P34_55

**Symbol:** SEI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 859 |
| net_profit_factor | 0.4420 |
| net_win_rate | 0.4366 |
| gross_profit_factor | 0.8033 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -7.9638 |
| sortino_ratio | -3.2908 |
| max_drawdown | 0.9847 |
| cagr | -0.8081 |
| net_avg_win | 20.7857 |
| net_avg_loss | -36.4388 |
| avg_hold_time_bars | 3.1281 |
| exposure | 0.1221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
