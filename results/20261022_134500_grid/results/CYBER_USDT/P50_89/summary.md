# EMA Hourly Continuation — CYBER/USDT P50_89

**Symbol:** CYBER/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.5520 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9599 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -4.3152 |
| sortino_ratio | -1.5734 |
| max_drawdown | 0.8561 |
| cagr | -0.5272 |
| net_avg_win | 32.0299 |
| net_avg_loss | -56.1351 |
| avg_hold_time_bars | 4.9744 |
| exposure | 0.1499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
