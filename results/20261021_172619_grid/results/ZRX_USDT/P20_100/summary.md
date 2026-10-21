# EMA Hourly Continuation — ZRX/USDT P20_100

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7947 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0381 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -1.6825 |
| sortino_ratio | -0.5467 |
| max_drawdown | 0.5086 |
| cagr | -0.2230 |
| net_avg_win | 69.6273 |
| net_avg_loss | -90.7388 |
| avg_hold_time_bars | 18.0663 |
| exposure | 0.4213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
