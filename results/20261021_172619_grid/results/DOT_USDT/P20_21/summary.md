# EMA Hourly Continuation — DOT/USDT P20_21

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 102 |
| net_profit_factor | 0.6624 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9246 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -1.2956 |
| sortino_ratio | -0.1876 |
| max_drawdown | 0.2216 |
| cagr | -0.0822 |
| net_avg_win | 77.5809 |
| net_avg_loss | -108.2776 |
| avg_hold_time_bars | 4.7941 |
| exposure | 0.0222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
