# EMA Hourly Continuation — SLP/USDT P20_144

**Symbol:** SLP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.6515 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.9520 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -3.7557 |
| sortino_ratio | -1.2895 |
| max_drawdown | 0.7916 |
| cagr | -0.4597 |
| net_avg_win | 52.9143 |
| net_avg_loss | -71.0054 |
| avg_hold_time_bars | 20.2215 |
| exposure | 0.5478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
