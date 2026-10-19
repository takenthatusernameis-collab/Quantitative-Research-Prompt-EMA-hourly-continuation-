# EMA Hourly Continuation — ZRO/USDT P20_100

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.6726 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9118 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -3.0871 |
| sortino_ratio | -1.1202 |
| max_drawdown | 0.7132 |
| cagr | -0.4102 |
| net_avg_win | 49.4785 |
| net_avg_loss | -68.0123 |
| avg_hold_time_bars | 14.1765 |
| exposure | 0.4246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
