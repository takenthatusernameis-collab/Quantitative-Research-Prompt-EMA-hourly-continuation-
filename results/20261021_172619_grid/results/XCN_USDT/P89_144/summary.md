# EMA Hourly Continuation — XCN/USDT P89_144

**Symbol:** XCN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.5799 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.7753 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -2.8924 |
| sortino_ratio | -0.6879 |
| max_drawdown | 0.5678 |
| cagr | -0.2710 |
| net_avg_win | 61.9981 |
| net_avg_loss | -82.5492 |
| avg_hold_time_bars | 8.6571 |
| exposure | 0.1102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
