# EMA Hourly Continuation — NFT/USDT P20_100

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.3170 |
| net_win_rate | 0.2527 |
| gross_profit_factor | 0.7249 |
| gross_win_rate | 0.2905 |
| sharpe_ratio | -18.4469 |
| sortino_ratio | -9.6257 |
| max_drawdown | 1.0000 |
| cagr | -0.9949 |
| net_avg_win | 15.4177 |
| net_avg_loss | -16.4502 |
| avg_hold_time_bars | 7.7565 |
| exposure | 0.4199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
