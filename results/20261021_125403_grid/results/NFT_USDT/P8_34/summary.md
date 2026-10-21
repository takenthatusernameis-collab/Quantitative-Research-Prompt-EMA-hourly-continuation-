# EMA Hourly Continuation — NFT/USDT P8_34

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.3547 |
| net_win_rate | 0.3056 |
| gross_profit_factor | 0.6197 |
| gross_win_rate | 0.3090 |
| sharpe_ratio | -9.9221 |
| sortino_ratio | -3.5202 |
| max_drawdown | 0.9861 |
| cagr | -0.8178 |
| net_avg_win | 30.1192 |
| net_avg_loss | -37.3655 |
| avg_hold_time_bars | 9.5569 |
| exposure | 0.2559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
