# EMA Hourly Continuation — ENJ/USDT P21_89

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.6295 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.9989 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -4.6673 |
| sortino_ratio | -1.7614 |
| max_drawdown | 0.8904 |
| cagr | -0.5714 |
| net_avg_win | 44.5477 |
| net_avg_loss | -61.7585 |
| avg_hold_time_bars | 11.7628 |
| exposure | 0.3855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
