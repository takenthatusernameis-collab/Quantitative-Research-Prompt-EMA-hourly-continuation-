# EMA Hourly Continuation — BABYDOGE/USDT P50_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 28 |
| net_profit_factor | 1.6157 |
| net_win_rate | 0.6429 |
| gross_profit_factor | 1.7848 |
| gross_win_rate | 0.6429 |
| sharpe_ratio | 0.7923 |
| sortino_ratio | 0.0636 |
| max_drawdown | 0.0530 |
| cagr | 0.0260 |
| net_avg_win | 97.6354 |
| net_avg_loss | -108.7742 |
| avg_hold_time_bars | 16.0714 |
| exposure | 0.0204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
