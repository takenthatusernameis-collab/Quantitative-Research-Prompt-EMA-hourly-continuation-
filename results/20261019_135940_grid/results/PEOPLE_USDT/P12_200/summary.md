# EMA Hourly Continuation — PEOPLE/USDT P12_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7443 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9864 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -1.6971 |
| sortino_ratio | -0.4445 |
| max_drawdown | 0.4555 |
| cagr | -0.1906 |
| net_avg_win | 71.2067 |
| net_avg_loss | -90.8369 |
| avg_hold_time_bars | 48.4524 |
| exposure | 0.7608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
