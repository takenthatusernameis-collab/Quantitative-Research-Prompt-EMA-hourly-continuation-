# EMA Hourly Continuation — MEW/USDT P50_55

**Symbol:** MEW/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 149 |
| net_profit_factor | 0.6219 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8699 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -1.8533 |
| sortino_ratio | -0.3233 |
| max_drawdown | 0.3169 |
| cagr | -0.1378 |
| net_avg_win | 74.0795 |
| net_avg_loss | -102.7452 |
| avg_hold_time_bars | 3.8926 |
| exposure | 0.0264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
