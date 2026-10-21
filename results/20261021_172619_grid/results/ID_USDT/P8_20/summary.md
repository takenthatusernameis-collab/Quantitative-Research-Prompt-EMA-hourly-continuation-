# EMA Hourly Continuation — ID/USDT P8_20

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 764 |
| net_profit_factor | 0.6515 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9582 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -3.9805 |
| sortino_ratio | -1.5737 |
| max_drawdown | 0.8476 |
| cagr | -0.5131 |
| net_avg_win | 42.4220 |
| net_avg_loss | -60.8241 |
| avg_hold_time_bars | 5.5942 |
| exposure | 0.1934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
