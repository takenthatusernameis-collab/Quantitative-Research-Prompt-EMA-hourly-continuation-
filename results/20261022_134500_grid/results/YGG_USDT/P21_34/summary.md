# EMA Hourly Continuation — YGG/USDT P21_34

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1135 |
| net_profit_factor | 0.4597 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.8511 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -9.6863 |
| sortino_ratio | -4.6109 |
| max_drawdown | 0.9969 |
| cagr | -0.8982 |
| net_avg_win | 17.6719 |
| net_avg_loss | -28.1697 |
| avg_hold_time_bars | 2.6546 |
| exposure | 0.1363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
