# EMA Hourly Continuation — ETN/USDT P89_144

**Symbol:** ETN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.5690 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7409 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -2.7523 |
| sortino_ratio | -0.6474 |
| max_drawdown | 0.5032 |
| cagr | -0.2582 |
| net_avg_win | 61.5414 |
| net_avg_loss | -83.2027 |
| avg_hold_time_bars | 7.0652 |
| exposure | 0.0883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
