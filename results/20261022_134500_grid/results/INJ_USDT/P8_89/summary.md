# EMA Hourly Continuation — INJ/USDT P8_89

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.6050 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8481 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -4.6752 |
| sortino_ratio | -1.7787 |
| max_drawdown | 0.8857 |
| cagr | -0.5731 |
| net_avg_win | 40.5767 |
| net_avg_loss | -55.4167 |
| avg_hold_time_bars | 18.9226 |
| exposure | 0.6330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
