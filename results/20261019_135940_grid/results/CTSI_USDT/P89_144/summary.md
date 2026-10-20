# EMA Hourly Continuation — CTSI/USDT P89_144

**Symbol:** CTSI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.5255 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -4.8068 |
| sortino_ratio | -1.6195 |
| max_drawdown | 0.8590 |
| cagr | -0.5385 |
| net_avg_win | 36.7662 |
| net_avg_loss | -59.1849 |
| avg_hold_time_bars | 5.1758 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
