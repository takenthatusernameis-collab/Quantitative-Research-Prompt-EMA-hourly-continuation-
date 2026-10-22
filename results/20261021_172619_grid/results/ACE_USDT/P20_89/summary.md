# EMA Hourly Continuation — ACE/USDT P20_89

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.7962 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.5378 |
| sortino_ratio | -0.4687 |
| max_drawdown | 0.4497 |
| cagr | -0.1947 |
| net_avg_win | 71.7815 |
| net_avg_loss | -90.9518 |
| avg_hold_time_bars | 19.1886 |
| exposure | 0.3960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
