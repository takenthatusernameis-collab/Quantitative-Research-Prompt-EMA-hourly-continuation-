# EMA Hourly Continuation — COTI/USDT P8_89

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.7382 |
| net_win_rate | 0.5006 |
| gross_profit_factor | 1.0451 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -2.9052 |
| sortino_ratio | -1.1385 |
| max_drawdown | 0.7557 |
| cagr | -0.4192 |
| net_avg_win | 54.2473 |
| net_avg_loss | -73.6753 |
| avg_hold_time_bars | 18.0517 |
| exposure | 0.6343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
