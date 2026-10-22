# EMA Hourly Continuation — RPL/USDT P12_100

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.8135 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9790 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.5306 |
| sortino_ratio | -0.4906 |
| max_drawdown | 0.5018 |
| cagr | -0.2038 |
| net_avg_win | 76.5751 |
| net_avg_loss | -91.2042 |
| avg_hold_time_bars | 25.0336 |
| exposure | 0.5732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
