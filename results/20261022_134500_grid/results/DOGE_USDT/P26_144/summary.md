# EMA Hourly Continuation — DOGE/USDT P26_144

**Symbol:** DOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.5904 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.9337 |
| sortino_ratio | -1.2430 |
| max_drawdown | 0.7877 |
| cagr | -0.4473 |
| net_avg_win | 48.1104 |
| net_avg_loss | -70.0220 |
| avg_hold_time_bars | 19.3685 |
| exposure | 0.4420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
