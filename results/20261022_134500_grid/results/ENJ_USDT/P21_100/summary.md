# EMA Hourly Continuation — ENJ/USDT P21_100

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.6349 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9958 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -4.0906 |
| sortino_ratio | -1.4958 |
| max_drawdown | 0.8504 |
| cagr | -0.5138 |
| net_avg_win | 44.4244 |
| net_avg_loss | -64.2835 |
| avg_hold_time_bars | 13.1971 |
| exposure | 0.4091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
