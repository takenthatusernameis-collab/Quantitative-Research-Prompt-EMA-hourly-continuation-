# EMA Hourly Continuation — W/USDT P26_34

**Symbol:** W/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.4152 |
| net_win_rate | 0.4177 |
| gross_profit_factor | 0.9373 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -10.3950 |
| sortino_ratio | -4.8541 |
| max_drawdown | 0.9980 |
| cagr | -0.9158 |
| net_avg_win | 15.7797 |
| net_avg_loss | -27.2605 |
| avg_hold_time_bars | 2.1051 |
| exposure | 0.1029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
