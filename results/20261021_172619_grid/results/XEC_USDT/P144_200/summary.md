# EMA Hourly Continuation — XEC/USDT P144_200

**Symbol:** XEC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.6164 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9479 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -2.2251 |
| sortino_ratio | -0.4869 |
| max_drawdown | 0.4421 |
| cagr | -0.1988 |
| net_avg_win | 60.3723 |
| net_avg_loss | -93.8319 |
| avg_hold_time_bars | 7.6481 |
| exposure | 0.0806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
