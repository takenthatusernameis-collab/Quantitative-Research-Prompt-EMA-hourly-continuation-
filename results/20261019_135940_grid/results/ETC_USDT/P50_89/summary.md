# EMA Hourly Continuation — ETC/USDT P50_89

**Symbol:** ETC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.3884 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.8820 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -6.6946 |
| sortino_ratio | -2.4075 |
| max_drawdown | 0.9554 |
| cagr | -0.7090 |
| net_avg_win | 19.7554 |
| net_avg_loss | -44.6126 |
| avg_hold_time_bars | 5.0350 |
| exposure | 0.1504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
