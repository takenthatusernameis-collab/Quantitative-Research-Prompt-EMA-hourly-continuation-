# EMA Hourly Continuation — NFT/USDT P21_34

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.2360 |
| net_win_rate | 0.2399 |
| gross_profit_factor | 0.4902 |
| gross_win_rate | 0.2500 |
| sharpe_ratio | -8.5559 |
| sortino_ratio | -2.2200 |
| max_drawdown | 0.9356 |
| cagr | -0.6645 |
| net_avg_win | 40.7120 |
| net_avg_loss | -54.4286 |
| avg_hold_time_bars | 6.9459 |
| exposure | 0.0935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
