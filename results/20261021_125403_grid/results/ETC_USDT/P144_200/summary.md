# EMA Hourly Continuation — ETC/USDT P144_200

**Symbol:** ETC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 197 |
| net_profit_factor | 0.6291 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9650 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.9827 |
| sortino_ratio | -0.4009 |
| max_drawdown | 0.3732 |
| cagr | -0.1667 |
| net_avg_win | 64.2408 |
| net_avg_loss | -99.0570 |
| avg_hold_time_bars | 7.2183 |
| exposure | 0.0646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
