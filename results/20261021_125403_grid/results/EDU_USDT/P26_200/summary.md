# EMA Hourly Continuation — EDU/USDT P26_200

**Symbol:** EDU/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7856 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -1.3504 |
| sortino_ratio | -0.3585 |
| max_drawdown | 0.3789 |
| cagr | -0.1535 |
| net_avg_win | 74.8544 |
| net_avg_loss | -88.4434 |
| avg_hold_time_bars | 36.0430 |
| exposure | 0.5692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
