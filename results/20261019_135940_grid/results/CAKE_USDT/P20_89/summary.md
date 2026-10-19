# EMA Hourly Continuation — CAKE/USDT P20_89

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.6492 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.1017 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -3.5610 |
| sortino_ratio | -1.2785 |
| max_drawdown | 0.8107 |
| cagr | -0.4629 |
| net_avg_win | 44.1827 |
| net_avg_loss | -69.5225 |
| avg_hold_time_bars | 13.0565 |
| exposure | 0.3887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
