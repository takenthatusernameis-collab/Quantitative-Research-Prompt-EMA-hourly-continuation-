# EMA Hourly Continuation — POKT/USDT P8_12

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1766 |
| net_profit_factor | 0.2550 |
| net_win_rate | 0.3245 |
| gross_profit_factor | 0.7697 |
| gross_win_rate | 0.3630 |
| sharpe_ratio | -17.9573 |
| sortino_ratio | -10.8169 |
| max_drawdown | 1.0000 |
| cagr | -0.9964 |
| net_avg_win | 5.9742 |
| net_avg_loss | -11.2516 |
| avg_hold_time_bars | 2.4015 |
| exposure | 0.1919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
