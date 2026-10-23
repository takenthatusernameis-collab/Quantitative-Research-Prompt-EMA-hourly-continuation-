# EMA Hourly Continuation — ETN/USDT P50_200

**Symbol:** ETN/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.5174 |
| net_win_rate | 0.4129 |
| gross_profit_factor | 0.7367 |
| gross_win_rate | 0.4196 |
| sharpe_ratio | -5.2773 |
| sortino_ratio | -1.7154 |
| max_drawdown | 0.8313 |
| cagr | -0.5615 |
| net_avg_win | 47.6951 |
| net_avg_loss | -64.8470 |
| avg_hold_time_bars | 13.9643 |
| exposure | 0.3398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
