# EMA Hourly Continuation — AGLD/USDT P21_100

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.6990 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8712 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -2.9601 |
| sortino_ratio | -0.9559 |
| max_drawdown | 0.7129 |
| cagr | -0.3557 |
| net_avg_win | 65.9300 |
| net_avg_loss | -78.3807 |
| avg_hold_time_bars | 17.9904 |
| exposure | 0.4234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
