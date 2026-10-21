# EMA Hourly Continuation — MANTA/USDT P34_100

**Symbol:** MANTA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6897 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8692 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -2.6531 |
| sortino_ratio | -0.7906 |
| max_drawdown | 0.6202 |
| cagr | -0.3048 |
| net_avg_win | 65.8719 |
| net_avg_loss | -81.4060 |
| avg_hold_time_bars | 12.7289 |
| exposure | 0.2540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
