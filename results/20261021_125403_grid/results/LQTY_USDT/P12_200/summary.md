# EMA Hourly Continuation — LQTY/USDT P12_200

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.8403 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0067 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -0.7807 |
| sortino_ratio | -0.1820 |
| max_drawdown | 0.2500 |
| cagr | -0.0820 |
| net_avg_win | 75.5986 |
| net_avg_loss | -92.7182 |
| avg_hold_time_bars | 64.1767 |
| exposure | 0.7725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
