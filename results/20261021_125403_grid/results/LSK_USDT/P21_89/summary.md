# EMA Hourly Continuation — LSK/USDT P21_89

**Symbol:** LSK/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.7044 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.6363 |
| sortino_ratio | -0.8623 |
| max_drawdown | 0.6478 |
| cagr | -0.3279 |
| net_avg_win | 59.4538 |
| net_avg_loss | -78.2225 |
| avg_hold_time_bars | 14.7205 |
| exposure | 0.3520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
