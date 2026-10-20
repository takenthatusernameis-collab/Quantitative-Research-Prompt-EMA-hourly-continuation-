# EMA Hourly Continuation — WAVES/USDT P50_55

**Symbol:** WAVES/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.1438 |
| net_win_rate | 0.2848 |
| gross_profit_factor | 0.5642 |
| gross_win_rate | 0.3808 |
| sharpe_ratio | -15.3128 |
| sortino_ratio | -7.0557 |
| max_drawdown | 0.9999 |
| cagr | -0.9798 |
| net_avg_win | 6.3611 |
| net_avg_loss | -17.6150 |
| avg_hold_time_bars | 2.1327 |
| exposure | 0.0899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
