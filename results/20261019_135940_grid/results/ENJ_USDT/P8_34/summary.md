# EMA Hourly Continuation — ENJ/USDT P8_34

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1359 |
| net_profit_factor | 0.5083 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.9077 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -8.1706 |
| sortino_ratio | -4.2369 |
| max_drawdown | 0.9947 |
| cagr | -0.8750 |
| net_avg_win | 16.6378 |
| net_avg_loss | -27.2985 |
| avg_hold_time_bars | 5.5960 |
| exposure | 0.3457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
