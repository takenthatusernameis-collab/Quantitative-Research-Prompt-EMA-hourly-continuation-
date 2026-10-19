# EMA Hourly Continuation — ZRO/USDT P20_89

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6935 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9585 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -3.0983 |
| sortino_ratio | -1.1756 |
| max_drawdown | 0.7327 |
| cagr | -0.4253 |
| net_avg_win | 50.4849 |
| net_avg_loss | -69.1820 |
| avg_hold_time_bars | 11.6942 |
| exposure | 0.3818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
