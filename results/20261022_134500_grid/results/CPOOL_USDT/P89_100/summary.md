# EMA Hourly Continuation — CPOOL/USDT P89_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.3429 |
| net_win_rate | 0.3742 |
| gross_profit_factor | 0.6706 |
| gross_win_rate | 0.3926 |
| sharpe_ratio | -9.1335 |
| sortino_ratio | -3.3261 |
| max_drawdown | 0.9876 |
| cagr | -0.8251 |
| net_avg_win | 21.1159 |
| net_avg_loss | -36.8304 |
| avg_hold_time_bars | 2.2040 |
| exposure | 0.0653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
