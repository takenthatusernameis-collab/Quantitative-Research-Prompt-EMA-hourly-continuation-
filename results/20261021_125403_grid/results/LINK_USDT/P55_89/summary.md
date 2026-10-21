# EMA Hourly Continuation — LINK/USDT P55_89

**Symbol:** LINK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.7991 |
| net_win_rate | 0.5261 |
| gross_profit_factor | 1.1159 |
| gross_win_rate | 0.5261 |
| sharpe_ratio | -1.0986 |
| sortino_ratio | -0.2502 |
| max_drawdown | 0.2575 |
| cagr | -0.1085 |
| net_avg_win | 76.1106 |
| net_avg_loss | -105.7375 |
| avg_hold_time_bars | 7.7149 |
| exposure | 0.0873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
