# EMA Hourly Continuation — UNI/USDT P50_100

**Symbol:** UNI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.5259 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9431 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -4.9579 |
| sortino_ratio | -1.7299 |
| max_drawdown | 0.8913 |
| cagr | -0.5808 |
| net_avg_win | 32.8136 |
| net_avg_loss | -57.2405 |
| avg_hold_time_bars | 6.1643 |
| exposure | 0.1757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
