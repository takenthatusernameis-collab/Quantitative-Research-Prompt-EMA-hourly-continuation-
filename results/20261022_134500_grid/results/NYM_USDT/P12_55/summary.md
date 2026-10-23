# EMA Hourly Continuation — NYM/USDT P12_55

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.3275 |
| net_win_rate | 0.3847 |
| gross_profit_factor | 0.7584 |
| gross_win_rate | 0.4150 |
| sharpe_ratio | -9.6847 |
| sortino_ratio | -3.9251 |
| max_drawdown | 0.9940 |
| cagr | -0.8687 |
| net_avg_win | 15.2661 |
| net_avg_loss | -29.1484 |
| avg_hold_time_bars | 11.8993 |
| exposure | 0.4457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
