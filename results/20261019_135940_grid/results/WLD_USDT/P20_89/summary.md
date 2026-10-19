# EMA Hourly Continuation — WLD/USDT P20_89

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.7944 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.0922 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -1.9598 |
| sortino_ratio | -0.7254 |
| max_drawdown | 0.6308 |
| cagr | -0.2905 |
| net_avg_win | 63.9700 |
| net_avg_loss | -86.4686 |
| avg_hold_time_bars | 12.4911 |
| exposure | 0.3827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
