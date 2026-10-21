# EMA Hourly Continuation — SUPER/USDT P20_144

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.9272 |
| net_win_rate | 0.5325 |
| gross_profit_factor | 1.1256 |
| gross_win_rate | 0.5325 |
| sharpe_ratio | -0.4077 |
| sortino_ratio | -0.1176 |
| max_drawdown | 0.2693 |
| cagr | -0.0577 |
| net_avg_win | 82.8652 |
| net_avg_loss | -101.7955 |
| avg_hold_time_bars | 28.7300 |
| exposure | 0.5224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
