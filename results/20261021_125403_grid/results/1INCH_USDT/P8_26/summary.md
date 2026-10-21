# EMA Hourly Continuation — 1INCH/USDT P8_26

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.6494 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9182 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -3.7448 |
| sortino_ratio | -1.4122 |
| max_drawdown | 0.8082 |
| cagr | -0.4769 |
| net_avg_win | 44.6913 |
| net_avg_loss | -63.6602 |
| avg_hold_time_bars | 6.5671 |
| exposure | 0.2069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
