# EMA Hourly Continuation — BCH/USDT P50_89

**Symbol:** BCH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.3690 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.7494 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -7.7278 |
| sortino_ratio | -2.8983 |
| max_drawdown | 0.9719 |
| cagr | -0.7587 |
| net_avg_win | 19.6638 |
| net_avg_loss | -38.6970 |
| avg_hold_time_bars | 4.5488 |
| exposure | 0.1420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
