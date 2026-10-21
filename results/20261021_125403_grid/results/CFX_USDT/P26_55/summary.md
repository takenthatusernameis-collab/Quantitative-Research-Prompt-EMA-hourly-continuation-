# EMA Hourly Continuation — CFX/USDT P26_55

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6204 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8354 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -2.9935 |
| sortino_ratio | -0.8614 |
| max_drawdown | 0.6391 |
| cagr | -0.3265 |
| net_avg_win | 55.3113 |
| net_avg_loss | -75.0319 |
| avg_hold_time_bars | 7.8673 |
| exposure | 0.1455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
