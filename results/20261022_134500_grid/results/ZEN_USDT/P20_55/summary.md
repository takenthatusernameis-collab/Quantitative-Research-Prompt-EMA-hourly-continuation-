# EMA Hourly Continuation — ZEN/USDT P20_55

**Symbol:** ZEN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.5090 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8910 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -6.9180 |
| sortino_ratio | -3.1025 |
| max_drawdown | 0.9799 |
| cagr | -0.7857 |
| net_avg_win | 21.6443 |
| net_avg_loss | -35.5475 |
| avg_hold_time_bars | 5.0845 |
| exposure | 0.2380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
