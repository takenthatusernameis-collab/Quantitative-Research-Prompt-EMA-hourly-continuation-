# EMA Hourly Continuation — JASMY/USDT P21_55

**Symbol:** JASMY/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.7915 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0101 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.4846 |
| sortino_ratio | -0.4551 |
| max_drawdown | 0.4316 |
| cagr | -0.1898 |
| net_avg_win | 67.4702 |
| net_avg_loss | -87.5130 |
| avg_hold_time_bars | 7.5285 |
| exposure | 0.1560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
