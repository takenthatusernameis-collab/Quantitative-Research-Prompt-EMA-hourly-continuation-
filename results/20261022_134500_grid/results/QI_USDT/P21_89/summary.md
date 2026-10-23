# EMA Hourly Continuation — QI/USDT P21_89

**Symbol:** QI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6342 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9908 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -3.7224 |
| sortino_ratio | -1.3417 |
| max_drawdown | 0.8046 |
| cagr | -0.4688 |
| net_avg_win | 43.6041 |
| net_avg_loss | -65.2562 |
| avg_hold_time_bars | 12.8771 |
| exposure | 0.3793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
