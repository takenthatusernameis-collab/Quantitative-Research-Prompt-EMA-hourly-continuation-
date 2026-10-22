# EMA Hourly Continuation — AR/USDT P21_89

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.5714 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8522 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -4.6570 |
| sortino_ratio | -1.7601 |
| max_drawdown | 0.8854 |
| cagr | -0.5742 |
| net_avg_win | 35.1277 |
| net_avg_loss | -52.0095 |
| avg_hold_time_bars | 10.3776 |
| exposure | 0.3448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
