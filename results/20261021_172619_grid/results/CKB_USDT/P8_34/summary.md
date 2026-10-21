# EMA Hourly Continuation — CKB/USDT P8_34

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 798 |
| net_profit_factor | 0.7373 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9553 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -3.4752 |
| sortino_ratio | -1.4013 |
| max_drawdown | 0.8173 |
| cagr | -0.4730 |
| net_avg_win | 59.3815 |
| net_avg_loss | -72.4874 |
| avg_hold_time_bars | 8.5125 |
| exposure | 0.3088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
