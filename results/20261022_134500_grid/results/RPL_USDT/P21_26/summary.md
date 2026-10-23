# EMA Hourly Continuation — RPL/USDT P21_26

**Symbol:** RPL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1088 |
| net_profit_factor | 0.2433 |
| net_win_rate | 0.3925 |
| gross_profit_factor | 0.7417 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -11.7802 |
| sortino_ratio | -5.5720 |
| max_drawdown | 0.9993 |
| cagr | -0.9427 |
| net_avg_win | 7.5249 |
| net_avg_loss | -19.9785 |
| avg_hold_time_bars | 2.8851 |
| exposure | 0.1421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
