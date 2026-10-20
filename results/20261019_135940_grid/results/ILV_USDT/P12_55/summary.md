# EMA Hourly Continuation — ILV/USDT P12_55

**Symbol:** ILV/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1002 |
| net_profit_factor | 0.5881 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9371 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -5.6707 |
| sortino_ratio | -2.5222 |
| max_drawdown | 0.9556 |
| cagr | -0.7039 |
| net_avg_win | 28.7066 |
| net_avg_loss | -43.8185 |
| avg_hold_time_bars | 8.0549 |
| exposure | 0.3669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
