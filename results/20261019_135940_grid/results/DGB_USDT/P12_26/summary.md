# EMA Hourly Continuation — DGB/USDT P12_26

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1528 |
| net_profit_factor | 0.3554 |
| net_win_rate | 0.3835 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4090 |
| sharpe_ratio | -13.7401 |
| sortino_ratio | -7.6105 |
| max_drawdown | 0.9999 |
| cagr | -0.9800 |
| net_avg_win | 9.4089 |
| net_avg_loss | -16.4682 |
| avg_hold_time_bars | 2.9143 |
| exposure | 0.2024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
