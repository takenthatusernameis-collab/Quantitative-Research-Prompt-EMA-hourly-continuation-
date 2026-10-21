# EMA Hourly Continuation — AVA/USDT P20_26

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 223 |
| net_profit_factor | 0.5598 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.8621 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -2.6462 |
| sortino_ratio | -0.5676 |
| max_drawdown | 0.5154 |
| cagr | -0.2287 |
| net_avg_win | 58.5920 |
| net_avg_loss | -91.4692 |
| avg_hold_time_bars | 4.4888 |
| exposure | 0.0455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
