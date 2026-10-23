# EMA Hourly Continuation — GTC/USDT P8_100

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6289 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8962 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -3.6719 |
| sortino_ratio | -1.3262 |
| max_drawdown | 0.8015 |
| cagr | -0.4637 |
| net_avg_win | 44.3863 |
| net_avg_loss | -60.0382 |
| avg_hold_time_bars | 21.2344 |
| exposure | 0.6341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
