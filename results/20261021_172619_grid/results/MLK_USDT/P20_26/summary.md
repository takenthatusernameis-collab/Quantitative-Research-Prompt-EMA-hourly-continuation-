# EMA Hourly Continuation — MLK/USDT P20_26

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.2917 |
| net_win_rate | 0.3028 |
| gross_profit_factor | 0.4869 |
| gross_win_rate | 0.3108 |
| sharpe_ratio | -5.9060 |
| sortino_ratio | -1.3354 |
| max_drawdown | 0.8078 |
| cagr | -0.4750 |
| net_avg_win | 43.5207 |
| net_avg_loss | -64.7935 |
| avg_hold_time_bars | 5.5538 |
| exposure | 0.0631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
