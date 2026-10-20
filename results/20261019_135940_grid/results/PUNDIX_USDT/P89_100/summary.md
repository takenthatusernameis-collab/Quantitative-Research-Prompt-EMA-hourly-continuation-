# EMA Hourly Continuation — PUNDIX/USDT P89_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.1858 |
| net_win_rate | 0.3402 |
| gross_profit_factor | 0.5729 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -10.1490 |
| sortino_ratio | -3.5773 |
| max_drawdown | 0.9913 |
| cagr | -0.8481 |
| net_avg_win | 11.4820 |
| net_avg_loss | -31.8691 |
| avg_hold_time_bars | 3.6304 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
