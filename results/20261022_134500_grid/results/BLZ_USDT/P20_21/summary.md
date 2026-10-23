# EMA Hourly Continuation — BLZ/USDT P20_21

**Symbol:** BLZ/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1244 |
| net_profit_factor | 0.1393 |
| net_win_rate | 0.2846 |
| gross_profit_factor | 0.6040 |
| gross_win_rate | 0.3641 |
| sharpe_ratio | -17.8038 |
| sortino_ratio | -9.3951 |
| max_drawdown | 1.0000 |
| cagr | -0.9944 |
| net_avg_win | 4.5709 |
| net_avg_loss | -13.0540 |
| avg_hold_time_bars | 2.7243 |
| exposure | 0.1534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
