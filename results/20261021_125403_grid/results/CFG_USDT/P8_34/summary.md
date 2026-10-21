# EMA Hourly Continuation — CFG/USDT P8_34

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.6680 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -3.1355 |
| sortino_ratio | -1.0397 |
| max_drawdown | 0.7115 |
| cagr | -0.3804 |
| net_avg_win | 56.9641 |
| net_avg_loss | -70.4492 |
| avg_hold_time_bars | 17.7289 |
| exposure | 0.4400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
