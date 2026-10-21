# EMA Hourly Continuation — ENJ/USDT P26_100

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.6475 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -3.7944 |
| sortino_ratio | -1.3554 |
| max_drawdown | 0.8196 |
| cagr | -0.4803 |
| net_avg_win | 46.9835 |
| net_avg_loss | -68.2388 |
| avg_hold_time_bars | 12.5966 |
| exposure | 0.3716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
