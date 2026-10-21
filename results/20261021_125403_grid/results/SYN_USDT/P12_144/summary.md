# EMA Hourly Continuation — SYN/USDT P12_144

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.9770 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1284 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | -0.0746 |
| sortino_ratio | -0.0205 |
| max_drawdown | 0.2384 |
| cagr | -0.0161 |
| net_avg_win | 87.9950 |
| net_avg_loss | -102.8598 |
| avg_hold_time_bars | 42.1630 |
| exposure | 0.6938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
