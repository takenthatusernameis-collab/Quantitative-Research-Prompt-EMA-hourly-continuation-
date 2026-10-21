# EMA Hourly Continuation — ROSE/USDT P12_200

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.9313 |
| net_win_rate | 0.5193 |
| gross_profit_factor | 1.0626 |
| gross_win_rate | 0.5193 |
| sharpe_ratio | -0.2977 |
| sortino_ratio | -0.0652 |
| max_drawdown | 0.1871 |
| cagr | -0.0328 |
| net_avg_win | 90.0189 |
| net_avg_loss | -104.4310 |
| avg_hold_time_bars | 75.6824 |
| exposure | 0.8015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
