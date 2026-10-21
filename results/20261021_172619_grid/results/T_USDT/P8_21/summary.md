# EMA Hourly Continuation — T/USDT P8_21

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.6398 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 1.0097 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -4.6534 |
| sortino_ratio | -1.8104 |
| max_drawdown | 0.8812 |
| cagr | -0.5654 |
| net_avg_win | 44.1711 |
| net_avg_loss | -63.1364 |
| avg_hold_time_bars | 6.7212 |
| exposure | 0.2248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
