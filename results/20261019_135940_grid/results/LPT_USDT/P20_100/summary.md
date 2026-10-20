# EMA Hourly Continuation — LPT/USDT P20_100

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.5569 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8200 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -5.1154 |
| sortino_ratio | -1.9621 |
| max_drawdown | 0.9082 |
| cagr | -0.6054 |
| net_avg_win | 34.5034 |
| net_avg_loss | -49.4751 |
| avg_hold_time_bars | 12.1350 |
| exposure | 0.4087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
