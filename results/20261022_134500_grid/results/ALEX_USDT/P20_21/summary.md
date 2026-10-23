# EMA Hourly Continuation — ALEX/USDT P20_21

**Symbol:** ALEX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1113 |
| net_profit_factor | 0.1600 |
| net_win_rate | 0.2336 |
| gross_profit_factor | 0.6765 |
| gross_win_rate | 0.2974 |
| sharpe_ratio | -18.1816 |
| sortino_ratio | -9.1420 |
| max_drawdown | 1.0000 |
| cagr | -0.9943 |
| net_avg_win | 7.3277 |
| net_avg_loss | -13.9568 |
| avg_hold_time_bars | 2.2210 |
| exposure | 0.1124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
