# EMA Hourly Continuation — YFI/USDT P20_89

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 804 |
| net_profit_factor | 0.5097 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.9749 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -6.6797 |
| sortino_ratio | -2.6413 |
| max_drawdown | 0.9670 |
| cagr | -0.7348 |
| net_avg_win | 27.7124 |
| net_avg_loss | -44.5261 |
| avg_hold_time_bars | 10.7823 |
| exposure | 0.3923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
