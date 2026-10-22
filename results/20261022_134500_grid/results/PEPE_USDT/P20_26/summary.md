# EMA Hourly Continuation — PEPE/USDT P20_26

**Symbol:** PEPE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1221 |
| net_profit_factor | 0.3011 |
| net_win_rate | 0.3554 |
| gross_profit_factor | 0.6990 |
| gross_win_rate | 0.3882 |
| sharpe_ratio | -14.4264 |
| sortino_ratio | -7.2891 |
| max_drawdown | 0.9999 |
| cagr | -0.9797 |
| net_avg_win | 9.9257 |
| net_avg_loss | -18.1794 |
| avg_hold_time_bars | 1.7666 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
