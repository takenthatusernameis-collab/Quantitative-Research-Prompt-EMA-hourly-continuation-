# EMA Hourly Continuation — CTC/USDT P89_200

**Symbol:** CTC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5837 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 1.0182 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -3.9889 |
| sortino_ratio | -1.1493 |
| max_drawdown | 0.7776 |
| cagr | -0.4263 |
| net_avg_win | 54.6458 |
| net_avg_loss | -81.3947 |
| avg_hold_time_bars | 10.3976 |
| exposure | 0.1961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
