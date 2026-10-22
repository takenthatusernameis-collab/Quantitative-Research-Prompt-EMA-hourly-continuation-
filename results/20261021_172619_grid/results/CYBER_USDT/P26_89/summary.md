# EMA Hourly Continuation — CYBER/USDT P26_89

**Symbol:** CYBER/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7088 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9186 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.4894 |
| sortino_ratio | -0.8204 |
| max_drawdown | 0.6294 |
| cagr | -0.3134 |
| net_avg_win | 57.8640 |
| net_avg_loss | -76.0170 |
| avg_hold_time_bars | 13.2814 |
| exposure | 0.3218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
