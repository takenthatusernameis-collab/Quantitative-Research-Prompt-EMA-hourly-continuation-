# EMA Hourly Continuation — BDX/USDT P8_100

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1417 |
| net_profit_factor | 0.3292 |
| net_win_rate | 0.2978 |
| gross_profit_factor | 0.7069 |
| gross_win_rate | 0.3550 |
| sharpe_ratio | -17.4668 |
| sortino_ratio | -9.5787 |
| max_drawdown | 1.0000 |
| cagr | -0.9944 |
| net_avg_win | 11.6288 |
| net_avg_loss | -14.9823 |
| avg_hold_time_bars | 6.7163 |
| exposure | 0.4326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
