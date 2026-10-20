# EMA Hourly Continuation — TRB/USDT P20_144

**Symbol:** TRB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.5913 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8485 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -3.7723 |
| sortino_ratio | -1.1823 |
| max_drawdown | 0.7614 |
| cagr | -0.4263 |
| net_avg_win | 48.6947 |
| net_avg_loss | -67.5681 |
| avg_hold_time_bars | 25.6217 |
| exposure | 0.5762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
