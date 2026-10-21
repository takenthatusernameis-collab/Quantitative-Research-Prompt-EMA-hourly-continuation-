# EMA Hourly Continuation — YFI/USDT P100_200

**Symbol:** YFI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.6290 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9227 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -2.3816 |
| sortino_ratio | -0.5929 |
| max_drawdown | 0.5199 |
| cagr | -0.2379 |
| net_avg_win | 57.2300 |
| net_avg_loss | -85.7325 |
| avg_hold_time_bars | 14.4125 |
| exposure | 0.1976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
