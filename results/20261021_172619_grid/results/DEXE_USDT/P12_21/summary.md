# EMA Hourly Continuation — DEXE/USDT P12_21

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.5871 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -2.7207 |
| sortino_ratio | -0.7086 |
| max_drawdown | 0.5707 |
| cagr | -0.2783 |
| net_avg_win | 50.6285 |
| net_avg_loss | -77.8137 |
| avg_hold_time_bars | 11.2870 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
