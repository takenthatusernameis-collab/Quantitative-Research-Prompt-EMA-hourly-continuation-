# EMA Hourly Continuation — BSV/USDT P34_55

**Symbol:** BSV/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 973 |
| net_profit_factor | 0.2771 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.6779 |
| gross_win_rate | 0.4193 |
| sharpe_ratio | -11.0841 |
| sortino_ratio | -4.9567 |
| max_drawdown | 0.9982 |
| cagr | -0.9180 |
| net_avg_win | 10.1212 |
| net_avg_loss | -23.2051 |
| avg_hold_time_bars | 3.5026 |
| exposure | 0.1549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
