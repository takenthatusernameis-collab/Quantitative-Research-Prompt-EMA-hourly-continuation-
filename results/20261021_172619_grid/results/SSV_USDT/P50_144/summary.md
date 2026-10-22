# EMA Hourly Continuation — SSV/USDT P50_144

**Symbol:** SSV/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6742 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8363 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -2.4772 |
| sortino_ratio | -0.6869 |
| max_drawdown | 0.5623 |
| cagr | -0.2703 |
| net_avg_win | 64.8410 |
| net_avg_loss | -80.5331 |
| avg_hold_time_bars | 15.9531 |
| exposure | 0.2772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
