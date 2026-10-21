# EMA Hourly Continuation — UQC/USDT P26_34

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 193 |
| net_profit_factor | 0.3415 |
| net_win_rate | 0.3161 |
| gross_profit_factor | 0.5276 |
| gross_win_rate | 0.3212 |
| sharpe_ratio | -4.7733 |
| sortino_ratio | -0.9347 |
| max_drawdown | 0.6779 |
| cagr | -0.3615 |
| net_avg_win | 57.5947 |
| net_avg_loss | -77.9350 |
| avg_hold_time_bars | 49.1762 |
| exposure | 0.4296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
