# EMA Hourly Continuation — ERG/USDT P21_89

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7043 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.8972 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -2.2009 |
| sortino_ratio | -0.6697 |
| max_drawdown | 0.5717 |
| cagr | -0.2654 |
| net_avg_win | 58.9036 |
| net_avg_loss | -76.9306 |
| avg_hold_time_bars | 15.6132 |
| exposure | 0.3229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
