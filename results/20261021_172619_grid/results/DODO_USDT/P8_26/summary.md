# EMA Hourly Continuation — DODO/USDT P8_26

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 804 |
| net_profit_factor | 0.6612 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.8959 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -3.6511 |
| sortino_ratio | -1.4755 |
| max_drawdown | 0.8178 |
| cagr | -0.4909 |
| net_avg_win | 41.8891 |
| net_avg_loss | -57.0638 |
| avg_hold_time_bars | 6.7861 |
| exposure | 0.2469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
