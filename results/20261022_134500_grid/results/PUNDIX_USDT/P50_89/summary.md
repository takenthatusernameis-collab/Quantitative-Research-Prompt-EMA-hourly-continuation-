# EMA Hourly Continuation — PUNDIX/USDT P50_89

**Symbol:** PUNDIX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.3647 |
| net_win_rate | 0.4169 |
| gross_profit_factor | 0.6927 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -6.8706 |
| sortino_ratio | -2.4402 |
| max_drawdown | 0.9507 |
| cagr | -0.6971 |
| net_avg_win | 20.9025 |
| net_avg_loss | -40.9792 |
| avg_hold_time_bars | 6.7348 |
| exposure | 0.1916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
