# EMA Hourly Continuation — XTZ/USDT P89_200

**Symbol:** XTZ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7069 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9440 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.6584 |
| sortino_ratio | -0.3971 |
| max_drawdown | 0.3884 |
| cagr | -0.1669 |
| net_avg_win | 64.2976 |
| net_avg_loss | -88.3903 |
| avg_hold_time_bars | 15.9357 |
| exposure | 0.2028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
