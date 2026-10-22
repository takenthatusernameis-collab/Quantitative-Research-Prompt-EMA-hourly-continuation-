# EMA Hourly Continuation — NOT/USDT P8_12

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.8227 |
| net_win_rate | 0.5210 |
| gross_profit_factor | 1.0822 |
| gross_win_rate | 0.5210 |
| sharpe_ratio | -0.7838 |
| sortino_ratio | -0.1484 |
| max_drawdown | 0.1823 |
| cagr | -0.0665 |
| net_avg_win | 82.1228 |
| net_avg_loss | -108.5605 |
| avg_hold_time_bars | 4.3832 |
| exposure | 0.0344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
