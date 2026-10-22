# EMA Hourly Continuation — GRT/USDT P21_55

**Symbol:** GRT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 920 |
| net_profit_factor | 0.5226 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8523 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -6.6082 |
| sortino_ratio | -2.8127 |
| max_drawdown | 0.9693 |
| cagr | -0.7469 |
| net_avg_win | 25.6102 |
| net_avg_loss | -40.0989 |
| avg_hold_time_bars | 5.0946 |
| exposure | 0.2121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
