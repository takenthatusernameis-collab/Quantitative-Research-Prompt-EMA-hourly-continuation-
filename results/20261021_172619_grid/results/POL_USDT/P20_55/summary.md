# EMA Hourly Continuation — POL/USDT P20_55

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6830 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9321 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.4482 |
| sortino_ratio | -0.7730 |
| max_drawdown | 0.6052 |
| cagr | -0.2988 |
| net_avg_win | 53.3914 |
| net_avg_loss | -75.0245 |
| avg_hold_time_bars | 10.5679 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
