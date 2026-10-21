# EMA Hourly Continuation — FLOKI/USDT P144_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 162 |
| net_profit_factor | 0.8837 |
| net_win_rate | 0.5432 |
| gross_profit_factor | 1.1770 |
| gross_win_rate | 0.5432 |
| sharpe_ratio | -0.4515 |
| sortino_ratio | -0.0832 |
| max_drawdown | 0.1154 |
| cagr | -0.0389 |
| net_avg_win | 81.8587 |
| net_avg_loss | -110.1538 |
| avg_hold_time_bars | 8.0370 |
| exposure | 0.0592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
