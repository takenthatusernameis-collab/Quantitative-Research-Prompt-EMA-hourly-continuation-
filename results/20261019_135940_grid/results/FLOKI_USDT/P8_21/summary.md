# EMA Hourly Continuation — FLOKI/USDT P8_21

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1735 |
| net_profit_factor | 0.4078 |
| net_win_rate | 0.4058 |
| gross_profit_factor | 0.7405 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -12.8956 |
| sortino_ratio | -7.5692 |
| max_drawdown | 0.9999 |
| cagr | -0.9785 |
| net_avg_win | 9.7819 |
| net_avg_loss | -16.3781 |
| avg_hold_time_bars | 2.7280 |
| exposure | 0.2151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
