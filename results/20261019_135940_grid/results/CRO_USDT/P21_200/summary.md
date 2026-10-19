# EMA Hourly Continuation — CRO/USDT P21_200

**Symbol:** CRO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.5188 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9066 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -3.1484 |
| sortino_ratio | -0.7891 |
| max_drawdown | 0.6490 |
| cagr | -0.3269 |
| net_avg_win | 43.2542 |
| net_avg_loss | -76.1037 |
| avg_hold_time_bars | 46.1520 |
| exposure | 0.6902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
