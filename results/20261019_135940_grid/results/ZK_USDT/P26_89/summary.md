# EMA Hourly Continuation — ZK/USDT P26_89

**Symbol:** ZK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.6898 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9920 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -3.8024 |
| sortino_ratio | -1.4625 |
| max_drawdown | 0.8098 |
| cagr | -0.5031 |
| net_avg_win | 53.6394 |
| net_avg_loss | -71.5444 |
| avg_hold_time_bars | 9.0230 |
| exposure | 0.3066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
