# EMA Hourly Continuation — XPR/USDT P21_55

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 856 |
| net_profit_factor | 0.4053 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.8116 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -8.9783 |
| sortino_ratio | -3.7121 |
| max_drawdown | 0.9921 |
| cagr | -0.8512 |
| net_avg_win | 19.0361 |
| net_avg_loss | -33.2819 |
| avg_hold_time_bars | 5.7862 |
| exposure | 0.2251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
