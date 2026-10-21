# EMA Hourly Continuation — YFI/USDT P21_200

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7720 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0041 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.4656 |
| sortino_ratio | -0.3907 |
| max_drawdown | 0.4211 |
| cagr | -0.1654 |
| net_avg_win | 70.4218 |
| net_avg_loss | -92.8077 |
| avg_hold_time_bars | 39.9542 |
| exposure | 0.6310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
