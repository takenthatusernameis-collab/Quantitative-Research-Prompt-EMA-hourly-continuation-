# EMA Hourly Continuation — CSPR/USDT P20_89

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7445 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9200 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -1.9786 |
| sortino_ratio | -0.6382 |
| max_drawdown | 0.5694 |
| cagr | -0.2551 |
| net_avg_win | 61.6657 |
| net_avg_loss | -77.4932 |
| avg_hold_time_bars | 13.5773 |
| exposure | 0.3154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
