# EMA Hourly Continuation — RUNE/USDT P12_26

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.5948 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.8425 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -3.3848 |
| sortino_ratio | -1.0263 |
| max_drawdown | 0.7087 |
| cagr | -0.3760 |
| net_avg_win | 48.7471 |
| net_avg_loss | -71.0756 |
| avg_hold_time_bars | 5.2956 |
| exposure | 0.1083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
