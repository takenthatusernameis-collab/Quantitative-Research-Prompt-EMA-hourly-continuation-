# EMA Hourly Continuation — KSM/USDT P8_200

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6209 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8691 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -3.0443 |
| sortino_ratio | -0.7973 |
| max_drawdown | 0.6460 |
| cagr | -0.3221 |
| net_avg_win | 63.0068 |
| net_avg_loss | -85.6246 |
| avg_hold_time_bars | 49.9520 |
| exposure | 0.8038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
