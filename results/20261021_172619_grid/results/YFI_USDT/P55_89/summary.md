# EMA Hourly Continuation — YFI/USDT P55_89

**Symbol:** YFI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6404 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 1.0101 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -2.9633 |
| sortino_ratio | -0.8247 |
| max_drawdown | 0.6399 |
| cagr | -0.3146 |
| net_avg_win | 59.1523 |
| net_avg_loss | -89.4598 |
| avg_hold_time_bars | 6.7128 |
| exposure | 0.1142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
