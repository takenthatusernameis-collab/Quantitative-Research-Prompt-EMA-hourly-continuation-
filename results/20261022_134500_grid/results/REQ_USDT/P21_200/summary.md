# EMA Hourly Continuation — REQ/USDT P21_200

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.4830 |
| net_win_rate | 0.3947 |
| gross_profit_factor | 0.8459 |
| gross_win_rate | 0.4230 |
| sharpe_ratio | -7.0328 |
| sortino_ratio | -2.5076 |
| max_drawdown | 0.9538 |
| cagr | -0.7060 |
| net_avg_win | 35.5065 |
| net_avg_loss | -47.9217 |
| avg_hold_time_bars | 18.6431 |
| exposure | 0.5390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
