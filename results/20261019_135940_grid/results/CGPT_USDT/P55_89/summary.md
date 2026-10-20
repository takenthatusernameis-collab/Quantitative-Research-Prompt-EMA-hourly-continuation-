# EMA Hourly Continuation — CGPT/USDT P55_89

**Symbol:** CGPT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.4541 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.8187 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -6.3704 |
| sortino_ratio | -2.2669 |
| max_drawdown | 0.9432 |
| cagr | -0.6769 |
| net_avg_win | 28.1734 |
| net_avg_loss | -47.9067 |
| avg_hold_time_bars | 4.2461 |
| exposure | 0.1231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
