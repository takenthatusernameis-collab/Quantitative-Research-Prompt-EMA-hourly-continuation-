# EMA Hourly Continuation — XYO/USDT P8_200

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.4866 |
| net_win_rate | 0.4134 |
| gross_profit_factor | 0.7464 |
| gross_win_rate | 0.4242 |
| sharpe_ratio | -5.5521 |
| sortino_ratio | -1.8295 |
| max_drawdown | 0.8957 |
| cagr | -0.5868 |
| net_avg_win | 36.9426 |
| net_avg_loss | -53.4893 |
| avg_hold_time_bars | 29.6245 |
| exposure | 0.7427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
