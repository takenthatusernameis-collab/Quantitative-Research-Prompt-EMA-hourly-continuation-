# EMA Hourly Continuation — MOCA/USDT P100_144

**Symbol:** MOCA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.6803 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -1.9169 |
| sortino_ratio | -0.4121 |
| max_drawdown | 0.3701 |
| cagr | -0.1732 |
| net_avg_win | 75.5461 |
| net_avg_loss | -103.7144 |
| avg_hold_time_bars | 7.6732 |
| exposure | 0.0789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
