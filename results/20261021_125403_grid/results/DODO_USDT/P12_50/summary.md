# EMA Hourly Continuation — DODO/USDT P12_50

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.7226 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -2.9658 |
| sortino_ratio | -1.1107 |
| max_drawdown | 0.7332 |
| cagr | -0.3997 |
| net_avg_win | 57.3133 |
| net_avg_loss | -71.6935 |
| avg_hold_time_bars | 10.0476 |
| exposure | 0.3151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
