# EMA Hourly Continuation — XRP/USDT P21_50

**Symbol:** XRP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1013 |
| net_profit_factor | 0.2858 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.8517 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -10.8704 |
| sortino_ratio | -4.9324 |
| max_drawdown | 0.9983 |
| cagr | -0.9212 |
| net_avg_win | 9.7891 |
| net_avg_loss | -23.1025 |
| avg_hold_time_bars | 4.1876 |
| exposure | 0.1928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
