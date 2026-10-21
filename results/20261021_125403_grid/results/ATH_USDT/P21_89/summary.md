# EMA Hourly Continuation — ATH/USDT P21_89

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8954 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0866 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.7258 |
| sortino_ratio | -0.2300 |
| max_drawdown | 0.2896 |
| cagr | -0.1048 |
| net_avg_win | 82.5425 |
| net_avg_loss | -101.1067 |
| avg_hold_time_bars | 14.1473 |
| exposure | 0.3120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
