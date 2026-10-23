# EMA Hourly Continuation — PEOPLE/USDT P55_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.4925 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.7540 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -5.3920 |
| sortino_ratio | -1.9941 |
| max_drawdown | 0.9099 |
| cagr | -0.6130 |
| net_avg_win | 28.6398 |
| net_avg_loss | -47.6306 |
| avg_hold_time_bars | 4.6257 |
| exposure | 0.1432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
