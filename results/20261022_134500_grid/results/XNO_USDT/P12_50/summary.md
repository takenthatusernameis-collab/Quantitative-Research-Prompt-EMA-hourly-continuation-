# EMA Hourly Continuation — XNO/USDT P12_50

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1275 |
| net_profit_factor | 0.4982 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.8356 |
| gross_win_rate | 0.4086 |
| sharpe_ratio | -9.8879 |
| sortino_ratio | -4.9748 |
| max_drawdown | 0.9978 |
| cagr | -0.9123 |
| net_avg_win | 19.5403 |
| net_avg_loss | -25.8916 |
| avg_hold_time_bars | 5.5804 |
| exposure | 0.3234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
