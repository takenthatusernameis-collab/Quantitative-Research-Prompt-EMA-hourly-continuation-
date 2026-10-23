# EMA Hourly Continuation — IO/USDT P8_34

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1315 |
| net_profit_factor | 0.5886 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.8690 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -6.9009 |
| sortino_ratio | -3.6332 |
| max_drawdown | 0.9836 |
| cagr | -0.8252 |
| net_avg_win | 23.3003 |
| net_avg_loss | -33.6283 |
| avg_hold_time_bars | 5.3992 |
| exposure | 0.3437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
