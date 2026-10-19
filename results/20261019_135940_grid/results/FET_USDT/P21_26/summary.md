# EMA Hourly Continuation — FET/USDT P21_26

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1211 |
| net_profit_factor | 0.2933 |
| net_win_rate | 0.3609 |
| gross_profit_factor | 0.7582 |
| gross_win_rate | 0.3972 |
| sharpe_ratio | -14.1322 |
| sortino_ratio | -7.1343 |
| max_drawdown | 0.9999 |
| cagr | -0.9770 |
| net_avg_win | 9.4955 |
| net_avg_loss | -18.2800 |
| avg_hold_time_bars | 1.6697 |
| exposure | 0.0919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
