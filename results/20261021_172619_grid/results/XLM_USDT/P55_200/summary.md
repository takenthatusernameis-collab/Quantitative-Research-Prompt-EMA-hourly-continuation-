# EMA Hourly Continuation — XLM/USDT P55_200

**Symbol:** XLM/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7156 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9642 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.6947 |
| sortino_ratio | -0.4053 |
| max_drawdown | 0.4265 |
| cagr | -0.1697 |
| net_avg_win | 68.0449 |
| net_avg_loss | -92.4064 |
| avg_hold_time_bars | 27.6036 |
| exposure | 0.3513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
