# EMA Hourly Continuation — YFI/USDT P20_21

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.3574 |
| net_win_rate | 0.3965 |
| gross_profit_factor | 0.6825 |
| gross_win_rate | 0.3965 |
| sharpe_ratio | -4.6668 |
| sortino_ratio | -1.0214 |
| max_drawdown | 0.7030 |
| cagr | -0.3784 |
| net_avg_win | 43.1772 |
| net_avg_loss | -79.3559 |
| avg_hold_time_bars | 4.8106 |
| exposure | 0.0494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
