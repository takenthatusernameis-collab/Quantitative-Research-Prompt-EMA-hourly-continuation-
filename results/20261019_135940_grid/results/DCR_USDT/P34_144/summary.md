# EMA Hourly Continuation — DCR/USDT P34_144

**Symbol:** DCR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.5534 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8288 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -4.2290 |
| sortino_ratio | -1.4225 |
| max_drawdown | 0.8247 |
| cagr | -0.4891 |
| net_avg_win | 39.6700 |
| net_avg_loss | -58.0270 |
| avg_hold_time_bars | 13.5509 |
| exposure | 0.3495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
