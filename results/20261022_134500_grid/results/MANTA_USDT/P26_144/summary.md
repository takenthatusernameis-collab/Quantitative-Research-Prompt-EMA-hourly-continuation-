# EMA Hourly Continuation — MANTA/USDT P26_144

**Symbol:** MANTA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.7030 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9322 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -2.3457 |
| sortino_ratio | -0.7029 |
| max_drawdown | 0.5655 |
| cagr | -0.2792 |
| net_avg_win | 62.0025 |
| net_avg_loss | -81.0032 |
| avg_hold_time_bars | 25.6465 |
| exposure | 0.5211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
