# EMA Hourly Continuation — ZK/USDT P26_144

**Symbol:** ZK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6854 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -3.1634 |
| sortino_ratio | -1.0570 |
| max_drawdown | 0.6939 |
| cagr | -0.3922 |
| net_avg_win | 61.4464 |
| net_avg_loss | -78.6912 |
| avg_hold_time_bars | 17.9579 |
| exposure | 0.4570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
