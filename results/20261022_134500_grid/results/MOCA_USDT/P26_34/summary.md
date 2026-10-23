# EMA Hourly Continuation — MOCA/USDT P26_34

**Symbol:** MOCA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 936 |
| net_profit_factor | 0.3023 |
| net_win_rate | 0.3675 |
| gross_profit_factor | 0.7129 |
| gross_win_rate | 0.4156 |
| sharpe_ratio | -12.2968 |
| sortino_ratio | -5.7169 |
| max_drawdown | 0.9988 |
| cagr | -0.9479 |
| net_avg_win | 12.5807 |
| net_avg_loss | -24.1820 |
| avg_hold_time_bars | 2.2660 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
