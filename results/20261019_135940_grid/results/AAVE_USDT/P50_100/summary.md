# EMA Hourly Continuation — AAVE/USDT P50_100

**Symbol:** AAVE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.4654 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8154 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -5.4508 |
| sortino_ratio | -1.9579 |
| max_drawdown | 0.9191 |
| cagr | -0.6200 |
| net_avg_win | 26.2016 |
| net_avg_loss | -48.3243 |
| avg_hold_time_bars | 5.4939 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
