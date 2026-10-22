# EMA Hourly Continuation — CRV/USDT P26_50

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 972 |
| net_profit_factor | 0.5031 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.9540 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -6.8417 |
| sortino_ratio | -3.0048 |
| max_drawdown | 0.9761 |
| cagr | -0.7711 |
| net_avg_win | 21.8025 |
| net_avg_loss | -37.8227 |
| avg_hold_time_bars | 3.2356 |
| exposure | 0.1430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
