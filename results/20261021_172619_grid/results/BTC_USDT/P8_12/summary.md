# EMA Hourly Continuation — BTC/USDT P8_12

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.6309 |
| net_win_rate | 0.5443 |
| gross_profit_factor | 1.3064 |
| gross_win_rate | 0.5696 |
| sharpe_ratio | -1.9730 |
| sortino_ratio | -0.4141 |
| max_drawdown | 0.4163 |
| cagr | -0.1719 |
| net_avg_win | 55.1674 |
| net_avg_loss | -104.4415 |
| avg_hold_time_bars | 5.4937 |
| exposure | 0.0521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
