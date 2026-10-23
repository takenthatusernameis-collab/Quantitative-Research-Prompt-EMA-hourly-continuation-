# EMA Hourly Continuation — TFUEL/USDT P34_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.4971 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.7754 |
| gross_win_rate | 0.4180 |
| sharpe_ratio | -6.1875 |
| sortino_ratio | -2.1834 |
| max_drawdown | 0.9316 |
| cagr | -0.6530 |
| net_avg_win | 35.5266 |
| net_avg_loss | -49.3568 |
| avg_hold_time_bars | 12.6420 |
| exposure | 0.3627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
