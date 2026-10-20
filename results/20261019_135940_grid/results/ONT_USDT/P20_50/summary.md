# EMA Hourly Continuation — ONT/USDT P20_50

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.5176 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.9295 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -7.6773 |
| sortino_ratio | -3.3644 |
| max_drawdown | 0.9855 |
| cagr | -0.8073 |
| net_avg_win | 25.2043 |
| net_avg_loss | -37.3692 |
| avg_hold_time_bars | 4.8000 |
| exposure | 0.2096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
