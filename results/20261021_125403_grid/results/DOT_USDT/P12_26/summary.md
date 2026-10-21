# EMA Hourly Continuation — DOT/USDT P12_26

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6428 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9209 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.7444 |
| sortino_ratio | -0.7879 |
| max_drawdown | 0.6075 |
| cagr | -0.3017 |
| net_avg_win | 55.6930 |
| net_avg_loss | -79.5891 |
| avg_hold_time_bars | 5.3491 |
| exposure | 0.0975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
