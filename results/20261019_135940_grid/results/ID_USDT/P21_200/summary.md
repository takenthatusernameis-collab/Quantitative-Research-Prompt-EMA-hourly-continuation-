# EMA Hourly Continuation — ID/USDT P21_200

**Symbol:** ID/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7362 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0192 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -1.6563 |
| sortino_ratio | -0.4464 |
| max_drawdown | 0.4355 |
| cagr | -0.1915 |
| net_avg_win | 62.2742 |
| net_avg_loss | -87.4039 |
| avg_hold_time_bars | 39.1311 |
| exposure | 0.6481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
