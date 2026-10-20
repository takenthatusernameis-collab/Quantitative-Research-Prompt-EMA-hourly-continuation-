# EMA Hourly Continuation — NOT/USDT P20_100

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.6325 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9481 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -3.9668 |
| sortino_ratio | -1.4835 |
| max_drawdown | 0.8290 |
| cagr | -0.5102 |
| net_avg_win | 42.8170 |
| net_avg_loss | -63.1190 |
| avg_hold_time_bars | 12.9548 |
| exposure | 0.4175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
