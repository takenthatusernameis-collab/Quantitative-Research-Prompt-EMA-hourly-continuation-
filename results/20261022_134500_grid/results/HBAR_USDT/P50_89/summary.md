# EMA Hourly Continuation — HBAR/USDT P50_89

**Symbol:** HBAR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.4483 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8963 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -6.5896 |
| sortino_ratio | -2.3661 |
| max_drawdown | 0.9494 |
| cagr | -0.6912 |
| net_avg_win | 26.9273 |
| net_avg_loss | -48.2536 |
| avg_hold_time_bars | 4.3474 |
| exposure | 0.1269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
