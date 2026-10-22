# EMA Hourly Continuation — BLZ/USDT P20_144

**Symbol:** BLZ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6127 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -3.2888 |
| sortino_ratio | -0.8886 |
| max_drawdown | 0.6758 |
| cagr | -0.3420 |
| net_avg_win | 63.2855 |
| net_avg_loss | -82.1262 |
| avg_hold_time_bars | 41.8370 |
| exposure | 0.6967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
