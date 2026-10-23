# EMA Hourly Continuation — AVA/USDT P26_200

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -2.9953 |
| sortino_ratio | -0.8701 |
| max_drawdown | 0.6771 |
| cagr | -0.3448 |
| net_avg_win | 46.0288 |
| net_avg_loss | -69.1709 |
| avg_hold_time_bars | 26.6891 |
| exposure | 0.5229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
