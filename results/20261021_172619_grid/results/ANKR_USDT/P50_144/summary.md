# EMA Hourly Continuation — ANKR/USDT P50_144

**Symbol:** ANKR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6522 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8548 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -2.7412 |
| sortino_ratio | -0.7468 |
| max_drawdown | 0.5823 |
| cagr | -0.2910 |
| net_avg_win | 64.9563 |
| net_avg_loss | -83.1583 |
| avg_hold_time_bars | 18.3406 |
| exposure | 0.3060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
