# EMA Hourly Continuation — SKL/USDT P20_55

**Symbol:** SKL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 991 |
| net_profit_factor | 0.5749 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -6.0686 |
| sortino_ratio | -2.7000 |
| max_drawdown | 0.9627 |
| cagr | -0.7240 |
| net_avg_win | 27.9985 |
| net_avg_loss | -42.8783 |
| avg_hold_time_bars | 5.4622 |
| exposure | 0.2460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
