# EMA Hourly Continuation — ERG/USDT P8_34

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.6696 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -3.5870 |
| sortino_ratio | -1.3135 |
| max_drawdown | 0.7909 |
| cagr | -0.4552 |
| net_avg_win | 51.6539 |
| net_avg_loss | -66.5229 |
| avg_hold_time_bars | 8.9246 |
| exposure | 0.2690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
