# EMA Hourly Continuation — ZRO/USDT P21_200

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8173 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9289 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.0335 |
| sortino_ratio | -0.2562 |
| max_drawdown | 0.2788 |
| cagr | -0.1130 |
| net_avg_win | 80.2529 |
| net_avg_loss | -92.0935 |
| avg_hold_time_bars | 44.8078 |
| exposure | 0.6163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
