# EMA Hourly Continuation — WLD/USDT P8_34

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1413 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9503 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -6.3205 |
| sortino_ratio | -3.3329 |
| max_drawdown | 0.9838 |
| cagr | -0.8028 |
| net_avg_win | 21.1212 |
| net_avg_loss | -33.1533 |
| avg_hold_time_bars | 5.0842 |
| exposure | 0.3265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
