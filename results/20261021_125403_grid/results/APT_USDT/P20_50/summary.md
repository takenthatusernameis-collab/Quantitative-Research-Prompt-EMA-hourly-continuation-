# EMA Hourly Continuation — APT/USDT P20_50

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7090 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9366 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.1151 |
| sortino_ratio | -0.6540 |
| max_drawdown | 0.5632 |
| cagr | -0.2588 |
| net_avg_win | 56.2345 |
| net_avg_loss | -76.6427 |
| avg_hold_time_bars | 7.8605 |
| exposure | 0.1665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
