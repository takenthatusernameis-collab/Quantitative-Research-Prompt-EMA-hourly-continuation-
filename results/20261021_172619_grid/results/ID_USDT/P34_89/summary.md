# EMA Hourly Continuation — ID/USDT P34_89

**Symbol:** ID/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6593 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8893 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.8883 |
| sortino_ratio | -0.9127 |
| max_drawdown | 0.6587 |
| cagr | -0.3422 |
| net_avg_win | 54.4034 |
| net_avg_loss | -73.3529 |
| avg_hold_time_bars | 9.8134 |
| exposure | 0.2189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
