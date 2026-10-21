# EMA Hourly Continuation — ATH/USDT P34_55

**Symbol:** ATH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.8658 |
| net_win_rate | 0.5361 |
| gross_profit_factor | 1.1529 |
| gross_win_rate | 0.5361 |
| sharpe_ratio | -0.7009 |
| sortino_ratio | -0.1697 |
| max_drawdown | 0.1907 |
| cagr | -0.0768 |
| net_avg_win | 78.4580 |
| net_avg_loss | -104.7347 |
| avg_hold_time_bars | 5.4791 |
| exposure | 0.0698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
