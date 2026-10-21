# EMA Hourly Continuation — TURBO/USDT P12_144

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.7481 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.5278 |
| sortino_ratio | -0.8324 |
| max_drawdown | 0.6101 |
| cagr | -0.3251 |
| net_avg_win | 75.3614 |
| net_avg_loss | -96.3720 |
| avg_hold_time_bars | 25.5332 |
| exposure | 0.6296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
