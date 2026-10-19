# EMA Hourly Continuation — SEI/USDT P21_26

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1163 |
| net_profit_factor | 0.2794 |
| net_win_rate | 0.3611 |
| gross_profit_factor | 0.7120 |
| gross_win_rate | 0.4015 |
| sharpe_ratio | -14.2584 |
| sortino_ratio | -7.1013 |
| max_drawdown | 0.9999 |
| cagr | -0.9770 |
| net_avg_win | 9.2306 |
| net_avg_loss | -18.6757 |
| avg_hold_time_bars | 1.7885 |
| exposure | 0.0945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
