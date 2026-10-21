# EMA Hourly Continuation — KNC/USDT P89_100

**Symbol:** KNC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.5302 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9157 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.8589 |
| sortino_ratio | -0.5836 |
| max_drawdown | 0.5278 |
| cagr | -0.2373 |
| net_avg_win | 58.6347 |
| net_avg_loss | -98.1889 |
| avg_hold_time_bars | 5.9059 |
| exposure | 0.0542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
