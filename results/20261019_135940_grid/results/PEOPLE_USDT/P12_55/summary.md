# EMA Hourly Continuation — PEOPLE/USDT P12_55

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 982 |
| net_profit_factor | 0.5561 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.8115 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -6.4160 |
| sortino_ratio | -2.8078 |
| max_drawdown | 0.9673 |
| cagr | -0.7421 |
| net_avg_win | 28.3138 |
| net_avg_loss | -39.3337 |
| avg_hold_time_bars | 8.9511 |
| exposure | 0.3978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
