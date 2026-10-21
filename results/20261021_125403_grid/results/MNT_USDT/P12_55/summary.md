# EMA Hourly Continuation — MNT/USDT P12_55

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.7163 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 0.9968 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -2.4579 |
| sortino_ratio | -0.8567 |
| max_drawdown | 0.6389 |
| cagr | -0.3257 |
| net_avg_win | 53.4116 |
| net_avg_loss | -75.3259 |
| avg_hold_time_bars | 14.1929 |
| exposure | 0.3813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
