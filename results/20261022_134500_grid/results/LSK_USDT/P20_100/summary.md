# EMA Hourly Continuation — LSK/USDT P20_100

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.6137 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -3.8194 |
| sortino_ratio | -1.3077 |
| max_drawdown | 0.7984 |
| cagr | -0.4591 |
| net_avg_win | 46.6177 |
| net_avg_loss | -64.4202 |
| avg_hold_time_bars | 16.2158 |
| exposure | 0.4305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
