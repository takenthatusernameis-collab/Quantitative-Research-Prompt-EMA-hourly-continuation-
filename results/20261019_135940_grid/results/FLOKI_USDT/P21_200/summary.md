# EMA Hourly Continuation — FLOKI/USDT P21_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.6328 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8654 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -2.7255 |
| sortino_ratio | -0.7316 |
| max_drawdown | 0.5940 |
| cagr | -0.2935 |
| net_avg_win | 59.7258 |
| net_avg_loss | -80.8946 |
| avg_hold_time_bars | 39.6841 |
| exposure | 0.6566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
