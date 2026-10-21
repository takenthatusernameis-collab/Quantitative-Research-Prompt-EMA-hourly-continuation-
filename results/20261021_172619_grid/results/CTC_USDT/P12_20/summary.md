# EMA Hourly Continuation — CTC/USDT P12_20

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.5858 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.8891 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -2.9261 |
| sortino_ratio | -0.8193 |
| max_drawdown | 0.6099 |
| cagr | -0.3126 |
| net_avg_win | 46.8814 |
| net_avg_loss | -74.7486 |
| avg_hold_time_bars | 6.0131 |
| exposure | 0.1041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
