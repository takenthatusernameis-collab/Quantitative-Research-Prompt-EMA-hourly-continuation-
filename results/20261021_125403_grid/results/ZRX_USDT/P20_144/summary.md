# EMA Hourly Continuation — ZRX/USDT P20_144

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.7967 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0033 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.4233 |
| sortino_ratio | -0.4213 |
| max_drawdown | 0.4144 |
| cagr | -0.1773 |
| net_avg_win | 70.5971 |
| net_avg_loss | -89.8698 |
| avg_hold_time_bars | 27.2272 |
| exposure | 0.5285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
