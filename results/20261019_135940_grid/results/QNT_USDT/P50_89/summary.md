# EMA Hourly Continuation — QNT/USDT P50_89

**Symbol:** QNT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 795 |
| net_profit_factor | 0.3769 |
| net_win_rate | 0.4176 |
| gross_profit_factor | 0.7438 |
| gross_win_rate | 0.4314 |
| sharpe_ratio | -8.2970 |
| sortino_ratio | -3.3078 |
| max_drawdown | 0.9858 |
| cagr | -0.8116 |
| net_avg_win | 17.9466 |
| net_avg_loss | -34.1408 |
| avg_hold_time_bars | 4.0164 |
| exposure | 0.1451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
