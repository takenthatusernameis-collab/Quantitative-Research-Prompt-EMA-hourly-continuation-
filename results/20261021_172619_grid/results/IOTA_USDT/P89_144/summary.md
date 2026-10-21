# EMA Hourly Continuation — IOTA/USDT P89_144

**Symbol:** IOTA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.7591 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 1.0179 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -1.5082 |
| sortino_ratio | -0.3592 |
| max_drawdown | 0.4229 |
| cagr | -0.1518 |
| net_avg_win | 77.3197 |
| net_avg_loss | -102.6039 |
| avg_hold_time_bars | 8.1164 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
