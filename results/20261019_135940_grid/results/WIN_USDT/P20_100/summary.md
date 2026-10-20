# EMA Hourly Continuation — WIN/USDT P20_100

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.4514 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8140 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -6.1203 |
| sortino_ratio | -2.1375 |
| max_drawdown | 0.9337 |
| cagr | -0.6593 |
| net_avg_win | 28.2259 |
| net_avg_loss | -48.7338 |
| avg_hold_time_bars | 15.2271 |
| exposure | 0.4298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
