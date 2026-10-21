# EMA Hourly Continuation — APE/USDT P34_100

**Symbol:** APE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7250 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -1.9741 |
| sortino_ratio | -0.5645 |
| max_drawdown | 0.4967 |
| cagr | -0.2287 |
| net_avg_win | 65.0952 |
| net_avg_loss | -84.1519 |
| avg_hold_time_bars | 15.7107 |
| exposure | 0.2864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
