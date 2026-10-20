# EMA Hourly Continuation — GTC/USDT P12_89

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.6379 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9291 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -3.8909 |
| sortino_ratio | -1.4385 |
| max_drawdown | 0.8254 |
| cagr | -0.4946 |
| net_avg_win | 44.8446 |
| net_avg_loss | -61.5169 |
| avg_hold_time_bars | 16.3464 |
| exposure | 0.5127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
