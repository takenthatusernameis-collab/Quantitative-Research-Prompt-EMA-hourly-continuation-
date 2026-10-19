# EMA Hourly Continuation — DCR/USDT P26_89

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 782 |
| net_profit_factor | 0.4597 |
| net_win_rate | 0.4258 |
| gross_profit_factor | 0.7341 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -6.4288 |
| sortino_ratio | -2.5344 |
| max_drawdown | 0.9554 |
| cagr | -0.7032 |
| net_avg_win | 24.3571 |
| net_avg_loss | -39.2960 |
| avg_hold_time_bars | 8.7020 |
| exposure | 0.3079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
