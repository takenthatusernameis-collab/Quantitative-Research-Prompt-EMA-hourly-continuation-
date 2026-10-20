# EMA Hourly Continuation — MEME/USDT P12_34

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1302 |
| net_profit_factor | 0.4950 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8651 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -8.5529 |
| sortino_ratio | -4.3520 |
| max_drawdown | 0.9952 |
| cagr | -0.8797 |
| net_avg_win | 17.0541 |
| net_avg_loss | -26.9943 |
| avg_hold_time_bars | 4.2166 |
| exposure | 0.2495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
