# EMA Hourly Continuation — QNT/USDT P26_100

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7885 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0584 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -1.6776 |
| sortino_ratio | -0.5611 |
| max_drawdown | 0.5316 |
| cagr | -0.2271 |
| net_avg_win | 63.6732 |
| net_avg_loss | -86.3171 |
| avg_hold_time_bars | 11.8926 |
| exposure | 0.2919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
