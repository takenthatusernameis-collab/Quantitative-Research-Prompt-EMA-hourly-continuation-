# EMA Hourly Continuation — LPT/USDT P8_34

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 815 |
| net_profit_factor | 0.7536 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -3.3656 |
| sortino_ratio | -1.3715 |
| max_drawdown | 0.8054 |
| cagr | -0.4682 |
| net_avg_win | 61.8979 |
| net_avg_loss | -76.4888 |
| avg_hold_time_bars | 7.6638 |
| exposure | 0.2839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
