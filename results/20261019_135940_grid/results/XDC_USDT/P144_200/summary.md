# EMA Hourly Continuation — XDC/USDT P144_200

**Symbol:** XDC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.1966 |
| net_win_rate | 0.3889 |
| gross_profit_factor | 0.6219 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -8.2313 |
| sortino_ratio | -2.5923 |
| max_drawdown | 0.9717 |
| cagr | -0.7583 |
| net_avg_win | 12.5785 |
| net_avg_loss | -40.7227 |
| avg_hold_time_bars | 3.2366 |
| exposure | 0.0715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
