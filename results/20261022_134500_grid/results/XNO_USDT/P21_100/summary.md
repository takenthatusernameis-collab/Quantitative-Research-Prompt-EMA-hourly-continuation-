# EMA Hourly Continuation — XNO/USDT P21_100

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 840 |
| net_profit_factor | 0.5325 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.8167 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -6.5709 |
| sortino_ratio | -2.6846 |
| max_drawdown | 0.9600 |
| cagr | -0.7220 |
| net_avg_win | 31.1534 |
| net_avg_loss | -41.9901 |
| avg_hold_time_bars | 10.0262 |
| exposure | 0.3828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
