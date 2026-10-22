# EMA Hourly Continuation — XRP/USDT P50_89

**Symbol:** XRP/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.2648 |
| net_win_rate | 0.4065 |
| gross_profit_factor | 0.7732 |
| gross_win_rate | 0.4466 |
| sharpe_ratio | -8.7906 |
| sortino_ratio | -3.2589 |
| max_drawdown | 0.9856 |
| cagr | -0.8145 |
| net_avg_win | 12.9530 |
| net_avg_loss | -33.5095 |
| avg_hold_time_bars | 4.9228 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
