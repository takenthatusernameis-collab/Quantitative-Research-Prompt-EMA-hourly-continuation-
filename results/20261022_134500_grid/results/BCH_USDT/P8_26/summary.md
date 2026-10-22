# EMA Hourly Continuation — BCH/USDT P8_26

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1503 |
| net_profit_factor | 0.2977 |
| net_win_rate | 0.4092 |
| gross_profit_factor | 0.7656 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -13.0943 |
| sortino_ratio | -7.2020 |
| max_drawdown | 0.9999 |
| cagr | -0.9762 |
| net_avg_win | 6.8921 |
| net_avg_loss | -16.0336 |
| avg_hold_time_bars | 4.0665 |
| exposure | 0.2778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
