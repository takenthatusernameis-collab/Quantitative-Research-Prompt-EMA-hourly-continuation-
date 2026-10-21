# EMA Hourly Continuation — EGLD/USDT P20_144

**Symbol:** EGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.8413 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0440 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -0.9367 |
| sortino_ratio | -0.2638 |
| max_drawdown | 0.3609 |
| cagr | -0.1167 |
| net_avg_win | 71.6931 |
| net_avg_loss | -90.7123 |
| avg_hold_time_bars | 30.2656 |
| exposure | 0.5283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
