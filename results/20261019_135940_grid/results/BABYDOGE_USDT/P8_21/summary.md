# EMA Hourly Continuation — BABYDOGE/USDT P8_21

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 33 |
| net_profit_factor | 1.3894 |
| net_win_rate | 0.6061 |
| gross_profit_factor | 1.5265 |
| gross_win_rate | 0.6061 |
| sharpe_ratio | 0.5987 |
| sortino_ratio | 0.0512 |
| max_drawdown | 0.0422 |
| cagr | 0.0211 |
| net_avg_win | 96.3521 |
| net_avg_loss | -106.6872 |
| avg_hold_time_bars | 6.0000 |
| exposure | 0.0090 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
