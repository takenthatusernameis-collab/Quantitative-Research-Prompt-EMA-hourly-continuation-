# EMA Hourly Continuation — FLR/USDT P144_200

**Symbol:** FLR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8486 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -2.5144 |
| sortino_ratio | -0.5175 |
| max_drawdown | 0.4673 |
| cagr | -0.2124 |
| net_avg_win | 68.1934 |
| net_avg_loss | -96.6408 |
| avg_hold_time_bars | 7.5217 |
| exposure | 0.0708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
