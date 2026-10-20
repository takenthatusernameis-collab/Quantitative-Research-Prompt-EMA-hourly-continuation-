# EMA Hourly Continuation — BAND/USDT P12_55

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 852 |
| net_profit_factor | 0.6494 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 1.0455 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -4.7189 |
| sortino_ratio | -1.9231 |
| max_drawdown | 0.9092 |
| cagr | -0.6073 |
| net_avg_win | 41.0067 |
| net_avg_loss | -58.2972 |
| avg_hold_time_bars | 10.6901 |
| exposure | 0.4121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
