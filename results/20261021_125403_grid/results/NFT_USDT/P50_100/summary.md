# EMA Hourly Continuation — NFT/USDT P50_100

**Symbol:** NFT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.3682 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.7165 |
| gross_win_rate | 0.3361 |
| sharpe_ratio | -7.3288 |
| sortino_ratio | -2.0422 |
| max_drawdown | 0.9155 |
| cagr | -0.6206 |
| net_avg_win | 43.9340 |
| net_avg_loss | -59.6644 |
| avg_hold_time_bars | 9.4821 |
| exposure | 0.1565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
