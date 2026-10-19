# EMA Hourly Continuation — XLM/USDT P55_89

**Symbol:** XLM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.3371 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9835 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -6.7799 |
| sortino_ratio | -2.4482 |
| max_drawdown | 0.9601 |
| cagr | -0.7194 |
| net_avg_win | 15.6299 |
| net_avg_loss | -40.8628 |
| avg_hold_time_bars | 4.2402 |
| exposure | 0.1284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
