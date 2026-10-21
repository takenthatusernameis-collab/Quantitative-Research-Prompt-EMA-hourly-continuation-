# EMA Hourly Continuation — XNO/USDT P89_200

**Symbol:** XNO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.6249 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.8022 |
| gross_win_rate | 0.4364 |
| sharpe_ratio | -2.9287 |
| sortino_ratio | -0.7724 |
| max_drawdown | 0.5908 |
| cagr | -0.2994 |
| net_avg_win | 65.1774 |
| net_avg_loss | -80.7688 |
| avg_hold_time_bars | 12.8092 |
| exposure | 0.2015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
