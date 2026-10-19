# EMA Hourly Continuation — BAT/USDT P12_144

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6429 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9736 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -2.7984 |
| sortino_ratio | -0.8672 |
| max_drawdown | 0.6849 |
| cagr | -0.3396 |
| net_avg_win | 49.1666 |
| net_avg_loss | -72.7894 |
| avg_hold_time_bars | 30.6852 |
| exposure | 0.6779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
