# EMA Hourly Continuation — TRB/USDT P8_26

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.6692 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8924 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -3.8376 |
| sortino_ratio | -1.4021 |
| max_drawdown | 0.8082 |
| cagr | -0.4750 |
| net_avg_win | 53.8011 |
| net_avg_loss | -67.8206 |
| avg_hold_time_bars | 7.2909 |
| exposure | 0.2177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
