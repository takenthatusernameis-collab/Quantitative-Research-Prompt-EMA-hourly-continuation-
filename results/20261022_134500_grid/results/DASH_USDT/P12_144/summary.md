# EMA Hourly Continuation — DASH/USDT P12_144

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5258 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8685 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -4.0573 |
| sortino_ratio | -1.2535 |
| max_drawdown | 0.7945 |
| cagr | -0.4555 |
| net_avg_win | 39.4445 |
| net_avg_loss | -61.8173 |
| avg_hold_time_bars | 30.6489 |
| exposure | 0.6785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
