# EMA Hourly Continuation — MASK/USDT P26_144

**Symbol:** MASK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.4761 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.7889 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -5.1654 |
| sortino_ratio | -1.7300 |
| max_drawdown | 0.8810 |
| cagr | -0.5671 |
| net_avg_win | 32.3030 |
| net_avg_loss | -52.6974 |
| avg_hold_time_bars | 17.7699 |
| exposure | 0.4564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
