# EMA Hourly Continuation — RUNE/USDT P8_144

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7418 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0475 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -1.7886 |
| sortino_ratio | -0.4810 |
| max_drawdown | 0.4772 |
| cagr | -0.2029 |
| net_avg_win | 68.9318 |
| net_avg_loss | -93.9633 |
| avg_hold_time_bars | 48.8194 |
| exposure | 0.7989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
