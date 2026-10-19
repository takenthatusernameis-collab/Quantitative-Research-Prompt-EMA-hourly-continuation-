# EMA Hourly Continuation — DCR/USDT P12_144

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6590 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9598 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -3.0846 |
| sortino_ratio | -1.1037 |
| max_drawdown | 0.7480 |
| cagr | -0.4060 |
| net_avg_win | 44.5834 |
| net_avg_loss | -65.5820 |
| avg_hold_time_bars | 20.9224 |
| exposure | 0.6097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
