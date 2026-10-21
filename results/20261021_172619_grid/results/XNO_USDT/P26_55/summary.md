# EMA Hourly Continuation — XNO/USDT P26_55

**Symbol:** XNO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6103 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.8216 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -3.4082 |
| sortino_ratio | -1.0310 |
| max_drawdown | 0.7110 |
| cagr | -0.3772 |
| net_avg_win | 53.9170 |
| net_avg_loss | -71.3879 |
| avg_hold_time_bars | 6.5752 |
| exposure | 0.1351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
