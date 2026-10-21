# EMA Hourly Continuation — W/USDT P26_55

**Symbol:** W/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.8748 |
| net_win_rate | 0.5284 |
| gross_profit_factor | 1.1269 |
| gross_win_rate | 0.5284 |
| sharpe_ratio | -0.9363 |
| sortino_ratio | -0.2892 |
| max_drawdown | 0.3875 |
| cagr | -0.1270 |
| net_avg_win | 83.4881 |
| net_avg_loss | -106.9207 |
| avg_hold_time_bars | 6.6572 |
| exposure | 0.1386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
