# EMA Hourly Continuation — NOT/USDT P20_89

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.8785 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0674 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -0.8022 |
| sortino_ratio | -0.2507 |
| max_drawdown | 0.2914 |
| cagr | -0.1125 |
| net_avg_win | 76.8125 |
| net_avg_loss | -94.6224 |
| avg_hold_time_bars | 16.0285 |
| exposure | 0.3433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
