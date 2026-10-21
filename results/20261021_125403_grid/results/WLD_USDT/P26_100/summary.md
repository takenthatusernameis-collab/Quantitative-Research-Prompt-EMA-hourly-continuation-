# EMA Hourly Continuation — WLD/USDT P26_100

**Symbol:** WLD/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.9830 |
| net_win_rate | 0.5411 |
| gross_profit_factor | 1.1673 |
| gross_win_rate | 0.5411 |
| sharpe_ratio | -0.0502 |
| sortino_ratio | -0.0148 |
| max_drawdown | 0.2538 |
| cagr | -0.0146 |
| net_avg_win | 93.2006 |
| net_avg_loss | -111.7809 |
| avg_hold_time_bars | 17.2271 |
| exposure | 0.3242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
