# EMA Hourly Continuation — OGN/USDT P21_55

**Symbol:** OGN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.6471 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9113 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -3.6036 |
| sortino_ratio | -1.2220 |
| max_drawdown | 0.7767 |
| cagr | -0.4293 |
| net_avg_win | 52.1800 |
| net_avg_loss | -71.0275 |
| avg_hold_time_bars | 8.1004 |
| exposure | 0.2082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
