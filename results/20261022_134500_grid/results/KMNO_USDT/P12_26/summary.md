# EMA Hourly Continuation — KMNO/USDT P12_26

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1162 |
| net_profit_factor | 0.4512 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8512 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -8.4380 |
| sortino_ratio | -4.0843 |
| max_drawdown | 0.9933 |
| cagr | -0.8678 |
| net_avg_win | 15.6434 |
| net_avg_loss | -28.2791 |
| avg_hold_time_bars | 3.4010 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
