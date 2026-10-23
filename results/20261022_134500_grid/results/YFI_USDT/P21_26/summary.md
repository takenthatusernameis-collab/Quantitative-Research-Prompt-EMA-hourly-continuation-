# EMA Hourly Continuation — YFI/USDT P21_26

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1347 |
| net_profit_factor | 0.1509 |
| net_win_rate | 0.3155 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -17.9227 |
| sortino_ratio | -9.8655 |
| max_drawdown | 1.0000 |
| cagr | -0.9954 |
| net_avg_win | 4.1808 |
| net_avg_loss | -12.7732 |
| avg_hold_time_bars | 2.0876 |
| exposure | 0.1272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
