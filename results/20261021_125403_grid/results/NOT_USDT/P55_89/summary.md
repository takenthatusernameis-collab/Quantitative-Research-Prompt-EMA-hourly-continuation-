# EMA Hourly Continuation — NOT/USDT P55_89

**Symbol:** NOT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.8063 |
| net_win_rate | 0.5171 |
| gross_profit_factor | 1.0554 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -1.0568 |
| sortino_ratio | -0.2509 |
| max_drawdown | 0.2779 |
| cagr | -0.1093 |
| net_avg_win | 75.0624 |
| net_avg_loss | -99.6915 |
| avg_hold_time_bars | 6.7186 |
| exposure | 0.0830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
