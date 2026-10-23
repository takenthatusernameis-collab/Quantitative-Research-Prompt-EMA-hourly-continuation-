# EMA Hourly Continuation — WEMIX/USDT P20_26

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1736 |
| net_profit_factor | 0.0987 |
| net_win_rate | 0.2235 |
| gross_profit_factor | 0.3494 |
| gross_win_rate | 0.2627 |
| sharpe_ratio | -24.1158 |
| sortino_ratio | -15.2804 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 2.8212 |
| net_avg_loss | -8.2304 |
| avg_hold_time_bars | 2.1763 |
| exposure | 0.1717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
