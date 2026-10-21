# EMA Hourly Continuation — XLM/USDT P20_200

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.7877 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0061 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.2452 |
| sortino_ratio | -0.3055 |
| max_drawdown | 0.3285 |
| cagr | -0.1318 |
| net_avg_win | 74.8800 |
| net_avg_loss | -96.3661 |
| avg_hold_time_bars | 46.6497 |
| exposure | 0.6234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
