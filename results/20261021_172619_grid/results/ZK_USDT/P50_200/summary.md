# EMA Hourly Continuation — ZK/USDT P50_200

**Symbol:** ZK/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7786 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9175 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -1.3665 |
| sortino_ratio | -0.3523 |
| max_drawdown | 0.3450 |
| cagr | -0.1506 |
| net_avg_win | 75.9954 |
| net_avg_loss | -90.8099 |
| avg_hold_time_bars | 27.2787 |
| exposure | 0.4056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
