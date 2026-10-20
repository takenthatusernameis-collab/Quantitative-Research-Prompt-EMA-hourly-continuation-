# EMA Hourly Continuation — WAVES/USDT P50_200

**Symbol:** WAVES/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.4602 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.7826 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -4.8330 |
| sortino_ratio | -1.4919 |
| max_drawdown | 0.8544 |
| cagr | -0.5266 |
| net_avg_win | 34.0682 |
| net_avg_loss | -55.8492 |
| avg_hold_time_bars | 15.9919 |
| exposure | 0.3584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
