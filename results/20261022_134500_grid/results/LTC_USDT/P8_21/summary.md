# EMA Hourly Continuation — LTC/USDT P8_21

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1634 |
| net_profit_factor | 0.2330 |
| net_win_rate | 0.4021 |
| gross_profit_factor | 0.8384 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -15.0741 |
| sortino_ratio | -8.7152 |
| max_drawdown | 1.0000 |
| cagr | -0.9900 |
| net_avg_win | 4.6239 |
| net_avg_loss | -13.3447 |
| avg_hold_time_bars | 2.9259 |
| exposure | 0.2173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
