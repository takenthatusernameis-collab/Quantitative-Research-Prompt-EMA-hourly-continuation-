# EMA Hourly Continuation — AERO/USDT P12_34

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1213 |
| net_profit_factor | 0.4690 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8175 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -7.4819 |
| sortino_ratio | -3.6448 |
| max_drawdown | 0.9900 |
| cagr | -0.8367 |
| net_avg_win | 15.7434 |
| net_avg_loss | -28.3160 |
| avg_hold_time_bars | 4.1245 |
| exposure | 0.2274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
