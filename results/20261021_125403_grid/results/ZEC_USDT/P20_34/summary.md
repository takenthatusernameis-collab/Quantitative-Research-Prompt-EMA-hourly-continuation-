# EMA Hourly Continuation — ZEC/USDT P20_34

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.7237 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9532 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -1.5711 |
| sortino_ratio | -0.3634 |
| max_drawdown | 0.3551 |
| cagr | -0.1539 |
| net_avg_win | 70.1020 |
| net_avg_loss | -93.2308 |
| avg_hold_time_bars | 5.6437 |
| exposure | 0.0670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
