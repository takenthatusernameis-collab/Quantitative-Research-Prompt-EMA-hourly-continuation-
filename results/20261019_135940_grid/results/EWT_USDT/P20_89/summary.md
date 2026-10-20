# EMA Hourly Continuation — EWT/USDT P20_89

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.4762 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.7275 |
| gross_win_rate | 0.4201 |
| sharpe_ratio | -6.3533 |
| sortino_ratio | -2.4143 |
| max_drawdown | 0.9495 |
| cagr | -0.6926 |
| net_avg_win | 28.4587 |
| net_avg_loss | -41.6231 |
| avg_hold_time_bars | 9.8753 |
| exposure | 0.3313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
