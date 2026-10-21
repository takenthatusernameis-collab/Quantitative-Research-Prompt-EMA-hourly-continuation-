# EMA Hourly Continuation — ORBS/USDT P50_144

**Symbol:** ORBS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7240 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 1.0043 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -2.4040 |
| sortino_ratio | -0.6755 |
| max_drawdown | 0.5982 |
| cagr | -0.2662 |
| net_avg_win | 75.7822 |
| net_avg_loss | -98.3636 |
| avg_hold_time_bars | 17.6062 |
| exposure | 0.3089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
