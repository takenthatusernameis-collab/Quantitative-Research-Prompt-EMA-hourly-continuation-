# EMA Hourly Continuation — COTI/USDT P12_144

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.9318 |
| net_win_rate | 0.5230 |
| gross_profit_factor | 1.0853 |
| gross_win_rate | 0.5230 |
| sharpe_ratio | -0.3959 |
| sortino_ratio | -0.1159 |
| max_drawdown | 0.2859 |
| cagr | -0.0572 |
| net_avg_win | 86.9626 |
| net_avg_loss | -102.3291 |
| avg_hold_time_bars | 34.6513 |
| exposure | 0.6505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
