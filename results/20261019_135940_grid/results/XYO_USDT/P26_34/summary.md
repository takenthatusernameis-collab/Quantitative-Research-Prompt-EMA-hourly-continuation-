# EMA Hourly Continuation — XYO/USDT P26_34

**Symbol:** XYO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1154 |
| net_profit_factor | 0.1990 |
| net_win_rate | 0.3189 |
| gross_profit_factor | 0.5998 |
| gross_win_rate | 0.3631 |
| sharpe_ratio | -15.4892 |
| sortino_ratio | -7.7313 |
| max_drawdown | 1.0000 |
| cagr | -0.9835 |
| net_avg_win | 6.7506 |
| net_avg_loss | -15.8828 |
| avg_hold_time_bars | 2.6222 |
| exposure | 0.1369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
