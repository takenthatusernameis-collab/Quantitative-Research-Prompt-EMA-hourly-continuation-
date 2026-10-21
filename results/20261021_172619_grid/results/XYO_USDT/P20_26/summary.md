# EMA Hourly Continuation — XYO/USDT P20_26

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.5551 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8795 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -3.3602 |
| sortino_ratio | -0.7935 |
| max_drawdown | 0.6186 |
| cagr | -0.3076 |
| net_avg_win | 61.3192 |
| net_avg_loss | -91.1833 |
| avg_hold_time_bars | 5.6103 |
| exposure | 0.0691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
