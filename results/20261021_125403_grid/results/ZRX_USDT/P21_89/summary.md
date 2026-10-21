# EMA Hourly Continuation — ZRX/USDT P21_89

**Symbol:** ZRX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7771 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 1.0175 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -1.9984 |
| sortino_ratio | -0.6602 |
| max_drawdown | 0.5975 |
| cagr | -0.2629 |
| net_avg_win | 69.8731 |
| net_avg_loss | -90.2545 |
| avg_hold_time_bars | 15.5779 |
| exposure | 0.3774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
