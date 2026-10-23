# EMA Hourly Continuation — LQTY/USDT P12_89

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.6767 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9857 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.9418 |
| sortino_ratio | -1.0395 |
| max_drawdown | 0.7286 |
| cagr | -0.3894 |
| net_avg_win | 47.7560 |
| net_avg_loss | -69.2433 |
| avg_hold_time_bars | 21.1492 |
| exposure | 0.6029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
