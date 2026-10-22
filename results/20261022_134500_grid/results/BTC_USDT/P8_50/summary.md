# EMA Hourly Continuation — BTC/USDT P8_50

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1165 |
| net_profit_factor | 0.3363 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.8971 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -10.2615 |
| sortino_ratio | -4.6350 |
| max_drawdown | 0.9990 |
| cagr | -0.9118 |
| net_avg_win | 10.2254 |
| net_avg_loss | -22.4653 |
| avg_hold_time_bars | 10.2918 |
| exposure | 0.4796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
