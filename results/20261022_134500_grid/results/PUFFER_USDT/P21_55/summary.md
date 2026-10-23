# EMA Hourly Continuation — PUFFER/USDT P21_55

**Symbol:** PUFFER/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.6617 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0208 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -3.7934 |
| sortino_ratio | -1.5887 |
| max_drawdown | 0.7891 |
| cagr | -0.5337 |
| net_avg_win | 43.1471 |
| net_avg_loss | -65.7616 |
| avg_hold_time_bars | 6.0324 |
| exposure | 0.2420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
