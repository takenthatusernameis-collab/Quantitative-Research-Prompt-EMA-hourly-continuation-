# EMA Hourly Continuation — SATS/USDT P8_12

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.6829 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9615 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.2782 |
| sortino_ratio | -0.5815 |
| max_drawdown | 0.4993 |
| cagr | -0.2366 |
| net_avg_win | 68.1936 |
| net_avg_loss | -93.2806 |
| avg_hold_time_bars | 4.6409 |
| exposure | 0.0678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
