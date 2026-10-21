# EMA Hourly Continuation — HTX/USDT P8_55

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.4973 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.8047 |
| gross_win_rate | 0.4191 |
| sharpe_ratio | -6.9067 |
| sortino_ratio | -2.5471 |
| max_drawdown | 0.9522 |
| cagr | -0.7005 |
| net_avg_win | 34.5006 |
| net_avg_loss | -48.8166 |
| avg_hold_time_bars | 16.4826 |
| exposure | 0.4930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
