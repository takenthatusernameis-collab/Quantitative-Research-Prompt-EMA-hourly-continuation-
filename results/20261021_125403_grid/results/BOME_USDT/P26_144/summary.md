# EMA Hourly Continuation — BOME/USDT P26_144

**Symbol:** BOME/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.9002 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0488 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -0.4980 |
| sortino_ratio | -0.1331 |
| max_drawdown | 0.2714 |
| cagr | -0.0633 |
| net_avg_win | 76.2531 |
| net_avg_loss | -90.7972 |
| avg_hold_time_bars | 30.0983 |
| exposure | 0.4734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
