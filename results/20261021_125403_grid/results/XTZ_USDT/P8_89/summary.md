# EMA Hourly Continuation — XTZ/USDT P8_89

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8593 |
| net_win_rate | 0.5259 |
| gross_profit_factor | 1.0991 |
| gross_win_rate | 0.5259 |
| sharpe_ratio | -0.9483 |
| sortino_ratio | -0.2944 |
| max_drawdown | 0.3289 |
| cagr | -0.1296 |
| net_avg_win | 73.6957 |
| net_avg_loss | -95.1156 |
| avg_hold_time_bars | 32.1336 |
| exposure | 0.6777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
