# EMA Hourly Continuation — ARB/USDT P20_100

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.9300 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1523 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -0.4014 |
| sortino_ratio | -0.1202 |
| max_drawdown | 0.2654 |
| cagr | -0.0593 |
| net_avg_win | 81.8687 |
| net_avg_loss | -102.6980 |
| avg_hold_time_bars | 22.2844 |
| exposure | 0.4345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
