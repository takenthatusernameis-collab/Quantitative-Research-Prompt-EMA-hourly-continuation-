# EMA Hourly Continuation — ZEN/USDT P20_200

**Symbol:** ZEN/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7735 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0595 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.4664 |
| sortino_ratio | -0.3753 |
| max_drawdown | 0.4117 |
| cagr | -0.1635 |
| net_avg_win | 73.4766 |
| net_avg_loss | -100.3638 |
| avg_hold_time_bars | 47.1896 |
| exposure | 0.7014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
