# EMA Hourly Continuation — SSV/USDT P8_12

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7064 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9770 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -2.2760 |
| sortino_ratio | -0.6141 |
| max_drawdown | 0.5252 |
| cagr | -0.2456 |
| net_avg_win | 70.7794 |
| net_avg_loss | -94.7176 |
| avg_hold_time_bars | 4.3455 |
| exposure | 0.0700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
