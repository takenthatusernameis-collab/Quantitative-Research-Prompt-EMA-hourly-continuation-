# EMA Hourly Continuation — SUI/USDT P34_89

**Symbol:** SUI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.9140 |
| net_win_rate | 0.5399 |
| gross_profit_factor | 1.1607 |
| gross_win_rate | 0.5399 |
| sharpe_ratio | -0.5035 |
| sortino_ratio | -0.1412 |
| max_drawdown | 0.2404 |
| cagr | -0.0670 |
| net_avg_win | 83.6287 |
| net_avg_loss | -107.3674 |
| avg_hold_time_bars | 11.3085 |
| exposure | 0.1933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
