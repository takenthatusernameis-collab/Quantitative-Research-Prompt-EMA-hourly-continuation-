# EMA Hourly Continuation — ONT/USDT P21_200

**Symbol:** ONT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7385 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8820 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -1.7028 |
| sortino_ratio | -0.4402 |
| max_drawdown | 0.4447 |
| cagr | -0.1840 |
| net_avg_win | 72.6523 |
| net_avg_loss | -87.1943 |
| avg_hold_time_bars | 38.3373 |
| exposure | 0.5760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
