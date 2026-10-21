# EMA Hourly Continuation — CARV/USDT P21_55

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7356 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0134 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.2566 |
| sortino_ratio | -0.7580 |
| max_drawdown | 0.5271 |
| cagr | -0.2930 |
| net_avg_win | 63.3088 |
| net_avg_loss | -86.4515 |
| avg_hold_time_bars | 9.7472 |
| exposure | 0.2430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
