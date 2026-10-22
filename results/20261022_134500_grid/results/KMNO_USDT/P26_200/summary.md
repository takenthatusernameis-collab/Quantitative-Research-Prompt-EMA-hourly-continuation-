# EMA Hourly Continuation — KMNO/USDT P26_200

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.6300 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8775 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -2.9252 |
| sortino_ratio | -0.7919 |
| max_drawdown | 0.6192 |
| cagr | -0.3168 |
| net_avg_win | 62.5789 |
| net_avg_loss | -81.2294 |
| avg_hold_time_bars | 30.6206 |
| exposure | 0.5217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
