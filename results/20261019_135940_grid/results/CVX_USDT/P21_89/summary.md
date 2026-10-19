# EMA Hourly Continuation — CVX/USDT P21_89

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.5684 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.8528 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -4.7386 |
| sortino_ratio | -1.7793 |
| max_drawdown | 0.8881 |
| cagr | -0.5796 |
| net_avg_win | 35.4905 |
| net_avg_loss | -52.0034 |
| avg_hold_time_bars | 10.4765 |
| exposure | 0.3448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
