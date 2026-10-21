# EMA Hourly Continuation — ARB/USDT P12_55

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.8292 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.0497 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -1.2562 |
| sortino_ratio | -0.4245 |
| max_drawdown | 0.4467 |
| cagr | -0.1795 |
| net_avg_win | 66.7005 |
| net_avg_loss | -85.8591 |
| avg_hold_time_bars | 13.8424 |
| exposure | 0.3473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
