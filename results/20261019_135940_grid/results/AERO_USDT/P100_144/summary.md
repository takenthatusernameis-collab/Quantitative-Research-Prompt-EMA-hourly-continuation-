# EMA Hourly Continuation — AERO/USDT P100_144

**Symbol:** AERO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.4228 |
| net_win_rate | 0.4169 |
| gross_profit_factor | 0.7636 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -5.3072 |
| sortino_ratio | -1.4975 |
| max_drawdown | 0.8480 |
| cagr | -0.5277 |
| net_avg_win | 36.9791 |
| net_avg_loss | -62.5215 |
| avg_hold_time_bars | 3.9529 |
| exposure | 0.0724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
