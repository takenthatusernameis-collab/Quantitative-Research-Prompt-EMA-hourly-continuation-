# EMA Hourly Continuation — GRAM/USDT P20_89

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6226 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8503 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -3.0772 |
| sortino_ratio | -0.9663 |
| max_drawdown | 0.6851 |
| cagr | -0.3578 |
| net_avg_win | 49.2137 |
| net_avg_loss | -68.4016 |
| avg_hold_time_bars | 15.3216 |
| exposure | 0.3378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
