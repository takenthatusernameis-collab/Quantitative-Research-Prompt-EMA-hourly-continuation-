# EMA Hourly Continuation — CTSI/USDT P26_144

**Symbol:** CTSI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7132 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.8924 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -2.4631 |
| sortino_ratio | -0.7151 |
| max_drawdown | 0.6018 |
| cagr | -0.2813 |
| net_avg_win | 72.6188 |
| net_avg_loss | -87.3444 |
| avg_hold_time_bars | 25.4713 |
| exposure | 0.4840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
