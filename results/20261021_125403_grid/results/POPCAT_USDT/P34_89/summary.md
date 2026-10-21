# EMA Hourly Continuation — POPCAT/USDT P34_89

**Symbol:** POPCAT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7640 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9227 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -1.8243 |
| sortino_ratio | -0.5488 |
| max_drawdown | 0.4219 |
| cagr | -0.2238 |
| net_avg_win | 74.1880 |
| net_avg_loss | -89.7837 |
| avg_hold_time_bars | 11.4517 |
| exposure | 0.2317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
