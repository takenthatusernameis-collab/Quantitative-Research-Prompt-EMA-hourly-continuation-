# EMA Hourly Continuation — WEMIX/USDT P34_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.3780 |
| net_win_rate | 0.3199 |
| gross_profit_factor | 0.5407 |
| gross_win_rate | 0.3280 |
| sharpe_ratio | -8.5857 |
| sortino_ratio | -3.0191 |
| max_drawdown | 0.9763 |
| cagr | -0.7733 |
| net_avg_win | 29.8086 |
| net_avg_loss | -37.0955 |
| avg_hold_time_bars | 19.3280 |
| exposure | 0.5465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
