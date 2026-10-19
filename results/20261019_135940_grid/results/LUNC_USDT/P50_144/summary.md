# EMA Hourly Continuation — LUNC/USDT P50_144

**Symbol:** LUNC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.5224 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8998 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -4.5060 |
| sortino_ratio | -1.5045 |
| max_drawdown | 0.8472 |
| cagr | -0.5143 |
| net_avg_win | 34.9340 |
| net_avg_loss | -58.9970 |
| avg_hold_time_bars | 10.7138 |
| exposure | 0.2722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
