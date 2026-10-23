# EMA Hourly Continuation — SLP/USDT P8_89

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.6294 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.9559 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -5.2375 |
| sortino_ratio | -2.1687 |
| max_drawdown | 0.9293 |
| cagr | -0.6468 |
| net_avg_win | 39.9425 |
| net_avg_loss | -52.9759 |
| avg_hold_time_bars | 15.7471 |
| exposure | 0.6199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
