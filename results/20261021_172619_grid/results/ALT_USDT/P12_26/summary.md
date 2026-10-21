# EMA Hourly Continuation — ALT/USDT P12_26

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.6071 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8296 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -3.9781 |
| sortino_ratio | -1.4206 |
| max_drawdown | 0.8133 |
| cagr | -0.4800 |
| net_avg_win | 43.5664 |
| net_avg_loss | -60.0136 |
| avg_hold_time_bars | 6.1768 |
| exposure | 0.1763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
