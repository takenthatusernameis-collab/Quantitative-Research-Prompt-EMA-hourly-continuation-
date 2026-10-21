# EMA Hourly Continuation — YFI/USDT P34_50

**Symbol:** YFI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.5566 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9520 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.5429 |
| sortino_ratio | -0.9890 |
| max_drawdown | 0.7009 |
| cagr | -0.3639 |
| net_avg_win | 46.6911 |
| net_avg_loss | -79.5342 |
| avg_hold_time_bars | 5.2234 |
| exposure | 0.0889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
