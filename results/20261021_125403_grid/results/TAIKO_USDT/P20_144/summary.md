# EMA Hourly Continuation — TAIKO/USDT P20_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.7835 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9557 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -1.4369 |
| sortino_ratio | -0.3802 |
| max_drawdown | 0.3907 |
| cagr | -0.1614 |
| net_avg_win | 77.7709 |
| net_avg_loss | -95.0807 |
| avg_hold_time_bars | 35.8462 |
| exposure | 0.5596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
