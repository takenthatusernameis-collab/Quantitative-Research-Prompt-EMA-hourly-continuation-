# EMA Hourly Continuation — ETHFI/USDT P21_26

**Symbol:** ETHFI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1235 |
| net_profit_factor | 0.3227 |
| net_win_rate | 0.3644 |
| gross_profit_factor | 0.8075 |
| gross_win_rate | 0.3895 |
| sharpe_ratio | -13.8585 |
| sortino_ratio | -7.0127 |
| max_drawdown | 0.9999 |
| cagr | -0.9751 |
| net_avg_win | 10.5890 |
| net_avg_loss | -18.8078 |
| avg_hold_time_bars | 2.0567 |
| exposure | 0.1155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
