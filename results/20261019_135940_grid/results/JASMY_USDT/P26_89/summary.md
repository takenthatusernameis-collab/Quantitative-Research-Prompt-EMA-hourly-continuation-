# EMA Hourly Continuation — JASMY/USDT P26_89

**Symbol:** JASMY/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 1.0019 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -3.7433 |
| sortino_ratio | -1.4086 |
| max_drawdown | 0.8344 |
| cagr | -0.4940 |
| net_avg_win | 41.7742 |
| net_avg_loss | -63.8289 |
| avg_hold_time_bars | 8.9638 |
| exposure | 0.2930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
