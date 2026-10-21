# EMA Hourly Continuation — GRAM/USDT P34_144

**Symbol:** GRAM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6448 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8443 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -2.5290 |
| sortino_ratio | -0.6945 |
| max_drawdown | 0.5863 |
| cagr | -0.2729 |
| net_avg_win | 57.7832 |
| net_avg_loss | -77.5199 |
| avg_hold_time_bars | 21.3083 |
| exposure | 0.3613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
