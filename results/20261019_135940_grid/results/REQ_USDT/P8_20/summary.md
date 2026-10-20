# EMA Hourly Continuation — REQ/USDT P8_20

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1719 |
| net_profit_factor | 0.3235 |
| net_win_rate | 0.3572 |
| gross_profit_factor | 0.8103 |
| gross_win_rate | 0.4095 |
| sharpe_ratio | -17.0701 |
| sortino_ratio | -10.2118 |
| max_drawdown | 1.0000 |
| cagr | -0.9952 |
| net_avg_win | 7.7889 |
| net_avg_loss | -13.3777 |
| avg_hold_time_bars | 3.2618 |
| exposure | 0.2549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
