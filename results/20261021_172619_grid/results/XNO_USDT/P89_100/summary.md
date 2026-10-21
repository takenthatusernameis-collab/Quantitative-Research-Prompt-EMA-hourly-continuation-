# EMA Hourly Continuation — XNO/USDT P89_100

**Symbol:** XNO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 130 |
| net_profit_factor | 0.4821 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.6793 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -2.5811 |
| sortino_ratio | -0.4184 |
| max_drawdown | 0.4010 |
| cagr | -0.1751 |
| net_avg_win | 68.6459 |
| net_avg_loss | -94.9178 |
| avg_hold_time_bars | 6.2923 |
| exposure | 0.0372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
