# EMA Hourly Continuation — ENJ/USDT P20_55

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.7292 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -2.5000 |
| sortino_ratio | -0.8280 |
| max_drawdown | 0.6474 |
| cagr | -0.3164 |
| net_avg_win | 63.1514 |
| net_avg_loss | -82.5300 |
| avg_hold_time_bars | 8.0371 |
| exposure | 0.1960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
