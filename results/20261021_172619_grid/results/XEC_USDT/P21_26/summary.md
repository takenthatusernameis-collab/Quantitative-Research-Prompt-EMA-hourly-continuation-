# EMA Hourly Continuation — XEC/USDT P21_26

**Symbol:** XEC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.5872 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.8933 |
| sortino_ratio | -0.7378 |
| max_drawdown | 0.5953 |
| cagr | -0.2859 |
| net_avg_win | 52.5166 |
| net_avg_loss | -87.1925 |
| avg_hold_time_bars | 5.0669 |
| exposure | 0.0720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
