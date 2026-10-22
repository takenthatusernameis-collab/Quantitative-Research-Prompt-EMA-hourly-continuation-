# EMA Hourly Continuation — XEC/USDT P89_200

**Symbol:** XEC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.4604 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.7839 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -5.0300 |
| sortino_ratio | -1.4446 |
| max_drawdown | 0.8379 |
| cagr | -0.5075 |
| net_avg_win | 40.5886 |
| net_avg_loss | -63.7503 |
| avg_hold_time_bars | 11.9928 |
| exposure | 0.2263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
