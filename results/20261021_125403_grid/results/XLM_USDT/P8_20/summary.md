# EMA Hourly Continuation — XLM/USDT P8_20

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6276 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 0.9699 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -2.7362 |
| sortino_ratio | -0.8307 |
| max_drawdown | 0.6200 |
| cagr | -0.3158 |
| net_avg_win | 46.4348 |
| net_avg_loss | -74.3212 |
| avg_hold_time_bars | 5.7865 |
| exposure | 0.1170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
