# EMA Hourly Continuation — UQC/USDT P12_144

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 190 |
| net_profit_factor | 0.3678 |
| net_win_rate | 0.3000 |
| gross_profit_factor | 0.4545 |
| gross_win_rate | 0.3000 |
| sharpe_ratio | -4.3707 |
| sortino_ratio | -0.8388 |
| max_drawdown | 0.6352 |
| cagr | -0.3278 |
| net_avg_win | 64.5820 |
| net_avg_loss | -75.2588 |
| avg_hold_time_bars | 87.4789 |
| exposure | 0.7523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
