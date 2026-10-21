# EMA Hourly Continuation — BTC/USDT P20_21

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 131 |
| net_profit_factor | 0.5176 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0613 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -2.0388 |
| sortino_ratio | -0.3170 |
| max_drawdown | 0.3411 |
| cagr | -0.1352 |
| net_avg_win | 55.1858 |
| net_avg_loss | -108.2591 |
| avg_hold_time_bars | 5.8550 |
| exposure | 0.0307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
