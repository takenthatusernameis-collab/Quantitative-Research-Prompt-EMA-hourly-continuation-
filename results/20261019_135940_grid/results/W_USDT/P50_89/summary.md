# EMA Hourly Continuation — W/USDT P50_89

**Symbol:** W/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.5557 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9132 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -4.3604 |
| sortino_ratio | -1.5762 |
| max_drawdown | 0.8621 |
| cagr | -0.5298 |
| net_avg_win | 33.7403 |
| net_avg_loss | -56.2512 |
| avg_hold_time_bars | 4.7008 |
| exposure | 0.1400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
