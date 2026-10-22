# EMA Hourly Continuation — ELON/USDT P144_200

**Symbol:** ELON/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.5675 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.7826 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -2.3076 |
| sortino_ratio | -0.4655 |
| max_drawdown | 0.4203 |
| cagr | -0.1923 |
| net_avg_win | 60.5352 |
| net_avg_loss | -87.2690 |
| avg_hold_time_bars | 7.2600 |
| exposure | 0.0660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
