# EMA Hourly Continuation — XNO/USDT P21_55

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.6626 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -3.1583 |
| sortino_ratio | -1.0227 |
| max_drawdown | 0.7237 |
| cagr | -0.3745 |
| net_avg_win | 57.1229 |
| net_avg_loss | -73.8017 |
| avg_hold_time_bars | 7.1027 |
| exposure | 0.1666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
