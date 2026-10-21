# EMA Hourly Continuation — HBAR/USDT P89_144

**Symbol:** HBAR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.7860 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0912 |
| gross_win_rate | 0.5182 |
| sharpe_ratio | -1.3595 |
| sortino_ratio | -0.3242 |
| max_drawdown | 0.4076 |
| cagr | -0.1385 |
| net_avg_win | 80.7737 |
| net_avg_loss | -110.5515 |
| avg_hold_time_bars | 7.6314 |
| exposure | 0.0950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
