# EMA Hourly Continuation — GMX/USDT P26_50

**Symbol:** GMX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.4311 |
| net_win_rate | 0.4086 |
| gross_profit_factor | 0.8302 |
| gross_win_rate | 0.4237 |
| sharpe_ratio | -8.7709 |
| sortino_ratio | -3.7900 |
| max_drawdown | 0.9908 |
| cagr | -0.8443 |
| net_avg_win | 19.7562 |
| net_avg_loss | -31.6612 |
| avg_hold_time_bars | 4.3226 |
| exposure | 0.1827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
