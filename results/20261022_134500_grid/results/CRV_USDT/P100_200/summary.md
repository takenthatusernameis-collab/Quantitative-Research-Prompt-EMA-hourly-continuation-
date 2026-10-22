# EMA Hourly Continuation — CRV/USDT P100_200

**Symbol:** CRV/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.5676 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9259 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -3.9935 |
| sortino_ratio | -1.2090 |
| max_drawdown | 0.7801 |
| cagr | -0.4470 |
| net_avg_win | 45.9733 |
| net_avg_loss | -72.7681 |
| avg_hold_time_bars | 6.7430 |
| exposure | 0.1431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
