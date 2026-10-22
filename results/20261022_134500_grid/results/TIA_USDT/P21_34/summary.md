# EMA Hourly Continuation — TIA/USDT P21_34

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1124 |
| net_profit_factor | 0.4957 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.9660 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -8.8585 |
| sortino_ratio | -4.1801 |
| max_drawdown | 0.9951 |
| cagr | -0.8773 |
| net_avg_win | 19.7927 |
| net_avg_loss | -31.3112 |
| avg_hold_time_bars | 2.6112 |
| exposure | 0.1334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
