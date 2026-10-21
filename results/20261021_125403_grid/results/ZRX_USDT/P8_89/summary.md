# EMA Hourly Continuation — ZRX/USDT P8_89

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.7474 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -2.1363 |
| sortino_ratio | -0.7171 |
| max_drawdown | 0.5847 |
| cagr | -0.2822 |
| net_avg_win | 61.7113 |
| net_avg_loss | -79.0635 |
| avg_hold_time_bars | 25.4693 |
| exposure | 0.6414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
