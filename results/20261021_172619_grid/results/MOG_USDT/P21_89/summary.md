# EMA Hourly Continuation — MOG/USDT P21_89

**Symbol:** MOG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.8547 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0041 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.0607 |
| sortino_ratio | -0.3260 |
| max_drawdown | 0.3799 |
| cagr | -0.1419 |
| net_avg_win | 82.2184 |
| net_avg_loss | -97.5793 |
| avg_hold_time_bars | 17.2494 |
| exposure | 0.3610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
