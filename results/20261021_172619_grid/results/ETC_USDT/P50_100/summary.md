# EMA Hourly Continuation — ETC/USDT P50_100

**Symbol:** ETC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.6529 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9563 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -2.3582 |
| sortino_ratio | -0.6258 |
| max_drawdown | 0.5207 |
| cagr | -0.2486 |
| net_avg_win | 57.0046 |
| net_avg_loss | -85.2922 |
| avg_hold_time_bars | 9.4825 |
| exposure | 0.1474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
