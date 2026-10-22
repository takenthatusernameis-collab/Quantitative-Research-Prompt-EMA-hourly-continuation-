# EMA Hourly Continuation — AAVE/USDT P55_200

**Symbol:** AAVE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.6657 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9674 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -2.4181 |
| sortino_ratio | -0.6965 |
| max_drawdown | 0.5966 |
| cagr | -0.2815 |
| net_avg_win | 54.5179 |
| net_avg_loss | -79.9568 |
| avg_hold_time_bars | 17.6403 |
| exposure | 0.3344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
