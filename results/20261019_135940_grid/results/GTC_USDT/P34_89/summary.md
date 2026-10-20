# EMA Hourly Continuation — GTC/USDT P34_89

**Symbol:** GTC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.5649 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8929 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -4.4667 |
| sortino_ratio | -1.6169 |
| max_drawdown | 0.8637 |
| cagr | -0.5324 |
| net_avg_win | 37.2292 |
| net_avg_loss | -54.8301 |
| avg_hold_time_bars | 8.7263 |
| exposure | 0.2594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
