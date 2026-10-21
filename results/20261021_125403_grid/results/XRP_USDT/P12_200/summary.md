# EMA Hourly Continuation — XRP/USDT P12_200

**Symbol:** XRP/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.7798 |
| net_win_rate | 0.5116 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -1.2093 |
| sortino_ratio | -0.3011 |
| max_drawdown | 0.3225 |
| cagr | -0.1298 |
| net_avg_win | 67.7602 |
| net_avg_loss | -91.0340 |
| avg_hold_time_bars | 51.9369 |
| exposure | 0.7106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
