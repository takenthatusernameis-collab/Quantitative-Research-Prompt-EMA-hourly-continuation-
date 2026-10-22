# EMA Hourly Continuation — ETHFI/USDT P20_34

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.4195 |
| net_win_rate | 0.4075 |
| gross_profit_factor | 0.8031 |
| gross_win_rate | 0.4194 |
| sharpe_ratio | -10.2061 |
| sortino_ratio | -4.9352 |
| max_drawdown | 0.9982 |
| cagr | -0.9182 |
| net_avg_win | 15.0303 |
| net_avg_loss | -24.6360 |
| avg_hold_time_bars | 2.9482 |
| exposure | 0.1579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
