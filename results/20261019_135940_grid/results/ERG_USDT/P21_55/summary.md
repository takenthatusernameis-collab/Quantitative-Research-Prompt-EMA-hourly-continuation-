# EMA Hourly Continuation — ERG/USDT P21_55

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.3536 |
| net_win_rate | 0.3811 |
| gross_profit_factor | 0.6480 |
| gross_win_rate | 0.4065 |
| sharpe_ratio | -9.6777 |
| sortino_ratio | -4.3108 |
| max_drawdown | 0.9954 |
| cagr | -0.8810 |
| net_avg_win | 14.5160 |
| net_avg_loss | -25.2805 |
| avg_hold_time_bars | 5.1494 |
| exposure | 0.2303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
