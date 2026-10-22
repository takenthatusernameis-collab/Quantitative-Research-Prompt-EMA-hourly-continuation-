# EMA Hourly Continuation — ZKJ/USDT P55_100

**Symbol:** ZKJ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.1654 |
| net_win_rate | 0.3590 |
| gross_profit_factor | 0.5186 |
| gross_win_rate | 0.4301 |
| sharpe_ratio | -11.5057 |
| sortino_ratio | -4.8022 |
| max_drawdown | 0.9985 |
| cagr | -0.9247 |
| net_avg_win | 6.5318 |
| net_avg_loss | -22.1146 |
| avg_hold_time_bars | 6.2808 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
