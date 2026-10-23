# EMA Hourly Continuation — BOSON/USDT P89_200

**Symbol:** BOSON/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7475 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9967 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -2.0241 |
| sortino_ratio | -0.5970 |
| max_drawdown | 0.5223 |
| cagr | -0.2413 |
| net_avg_win | 70.4842 |
| net_avg_loss | -90.8377 |
| avg_hold_time_bars | 10.6659 |
| exposure | 0.2075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
