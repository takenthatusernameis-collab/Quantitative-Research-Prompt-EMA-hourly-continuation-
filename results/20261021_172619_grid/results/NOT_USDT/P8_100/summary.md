# EMA Hourly Continuation — NOT/USDT P8_100

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.8943 |
| net_win_rate | 0.5191 |
| gross_profit_factor | 1.0617 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -0.5839 |
| sortino_ratio | -0.1577 |
| max_drawdown | 0.2802 |
| cagr | -0.0733 |
| net_avg_win | 80.7367 |
| net_avg_loss | -97.4405 |
| avg_hold_time_bars | 44.7654 |
| exposure | 0.7171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
