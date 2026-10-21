# EMA Hourly Continuation — TFUEL/USDT P50_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.4964 |
| net_win_rate | 0.4026 |
| gross_profit_factor | 0.7021 |
| gross_win_rate | 0.4026 |
| sharpe_ratio | -4.5403 |
| sortino_ratio | -1.2647 |
| max_drawdown | 0.7734 |
| cagr | -0.4428 |
| net_avg_win | 49.0538 |
| net_avg_loss | -66.5935 |
| avg_hold_time_bars | 7.3584 |
| exposure | 0.1282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
