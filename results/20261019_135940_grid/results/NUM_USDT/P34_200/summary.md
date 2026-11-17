# EMA Hourly Continuation — NUM/USDT P34_200

**Symbol:** NUM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.5292 |
| net_win_rate | 0.4148 |
| gross_profit_factor | 0.7025 |
| gross_win_rate | 0.4198 |
| sharpe_ratio | -3.8252 |
| sortino_ratio | -1.0782 |
| max_drawdown | 0.7369 |
| cagr | -0.4002 |
| net_avg_win | 48.3677 |
| net_avg_loss | -64.7904 |
| avg_hold_time_bars | 27.6815 |
| exposure | 0.5096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
