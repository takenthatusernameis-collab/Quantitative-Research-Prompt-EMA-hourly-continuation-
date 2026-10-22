# EMA Hourly Continuation — FLIP/USDT P12_26

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.4992 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.8450 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -5.6103 |
| sortino_ratio | -1.8815 |
| max_drawdown | 0.9000 |
| cagr | -0.5980 |
| net_avg_win | 36.4121 |
| net_avg_loss | -57.3267 |
| avg_hold_time_bars | 8.3274 |
| exposure | 0.2116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
