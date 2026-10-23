# EMA Hourly Continuation — ERG/USDT P21_34

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1167 |
| net_profit_factor | 0.1798 |
| net_win_rate | 0.3033 |
| gross_profit_factor | 0.4079 |
| gross_win_rate | 0.3282 |
| sharpe_ratio | -15.4036 |
| sortino_ratio | -7.6555 |
| max_drawdown | 1.0000 |
| cagr | -0.9820 |
| net_avg_win | 6.1917 |
| net_avg_loss | -14.9956 |
| avg_hold_time_bars | 2.7009 |
| exposure | 0.1433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
