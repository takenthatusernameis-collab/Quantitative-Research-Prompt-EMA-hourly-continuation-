# EMA Hourly Continuation — ICP/USDT P8_100

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6236 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9512 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -3.8213 |
| sortino_ratio | -1.3534 |
| max_drawdown | 0.8208 |
| cagr | -0.4848 |
| net_avg_win | 43.4846 |
| net_avg_loss | -64.3145 |
| avg_hold_time_bars | 23.4938 |
| exposure | 0.6877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
