# EMA Hourly Continuation — PEOPLE/USDT P12_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.5992 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 0.8334 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -4.2086 |
| sortino_ratio | -1.5064 |
| max_drawdown | 0.8419 |
| cagr | -0.5099 |
| net_avg_win | 42.8739 |
| net_avg_loss | -57.9999 |
| avg_hold_time_bars | 19.5031 |
| exposure | 0.5736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
