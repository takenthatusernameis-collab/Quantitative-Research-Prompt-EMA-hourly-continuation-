# EMA Hourly Continuation — ALGO/USDT P55_89

**Symbol:** ALGO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.4725 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -5.4356 |
| sortino_ratio | -1.9413 |
| max_drawdown | 0.9121 |
| cagr | -0.6131 |
| net_avg_win | 26.9256 |
| net_avg_loss | -51.2216 |
| avg_hold_time_bars | 3.9749 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
