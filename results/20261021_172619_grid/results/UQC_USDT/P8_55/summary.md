# EMA Hourly Continuation — UQC/USDT P8_55

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.3967 |
| net_win_rate | 0.3264 |
| gross_profit_factor | 0.5602 |
| gross_win_rate | 0.3299 |
| sharpe_ratio | -5.1755 |
| sortino_ratio | -1.2209 |
| max_drawdown | 0.7709 |
| cagr | -0.4421 |
| net_avg_win | 53.8913 |
| net_avg_loss | -65.8314 |
| avg_hold_time_bars | 51.9757 |
| exposure | 0.6775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
