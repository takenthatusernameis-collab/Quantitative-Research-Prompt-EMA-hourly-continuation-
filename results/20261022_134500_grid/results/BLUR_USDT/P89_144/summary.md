# EMA Hourly Continuation — BLUR/USDT P89_144

**Symbol:** BLUR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.6423 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0621 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -3.1110 |
| sortino_ratio | -0.9692 |
| max_drawdown | 0.6860 |
| cagr | -0.3661 |
| net_avg_win | 50.9121 |
| net_avg_loss | -79.5982 |
| avg_hold_time_bars | 5.5468 |
| exposure | 0.1207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
