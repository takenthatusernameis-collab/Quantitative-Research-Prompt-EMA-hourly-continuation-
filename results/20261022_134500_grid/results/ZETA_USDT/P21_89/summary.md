# EMA Hourly Continuation — ZETA/USDT P21_89

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.7154 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 1.0464 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -3.6674 |
| sortino_ratio | -1.3476 |
| max_drawdown | 0.8273 |
| cagr | -0.4751 |
| net_avg_win | 60.8108 |
| net_avg_loss | -79.9496 |
| avg_hold_time_bars | 12.6219 |
| exposure | 0.3912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
