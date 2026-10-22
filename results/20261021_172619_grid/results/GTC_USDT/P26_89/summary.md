# EMA Hourly Continuation — GTC/USDT P26_89

**Symbol:** GTC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.7400 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9393 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -2.0809 |
| sortino_ratio | -0.6647 |
| max_drawdown | 0.5575 |
| cagr | -0.2639 |
| net_avg_win | 62.6088 |
| net_avg_loss | -80.3272 |
| avg_hold_time_bars | 13.1517 |
| exposure | 0.2995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
