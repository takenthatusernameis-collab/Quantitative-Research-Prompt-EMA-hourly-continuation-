# EMA Hourly Continuation — CTC/USDT P89_200

**Symbol:** CTC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7641 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0368 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -1.4549 |
| sortino_ratio | -0.3526 |
| max_drawdown | 0.4272 |
| cagr | -0.1496 |
| net_avg_win | 74.7051 |
| net_avg_loss | -101.2556 |
| avg_hold_time_bars | 14.1965 |
| exposure | 0.1839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
