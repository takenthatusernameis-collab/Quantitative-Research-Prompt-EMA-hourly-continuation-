# EMA Hourly Continuation — LUNA/USDT P21_144

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.8024 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0039 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -1.3234 |
| sortino_ratio | -0.3799 |
| max_drawdown | 0.3653 |
| cagr | -0.1614 |
| net_avg_win | 71.8189 |
| net_avg_loss | -90.8533 |
| avg_hold_time_bars | 25.0499 |
| exposure | 0.4566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
