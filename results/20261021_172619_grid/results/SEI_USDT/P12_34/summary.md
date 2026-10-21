# EMA Hourly Continuation — SEI/USDT P12_34

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.7869 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0341 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.8465 |
| sortino_ratio | -0.6310 |
| max_drawdown | 0.5298 |
| cagr | -0.2514 |
| net_avg_win | 66.4862 |
| net_avg_loss | -87.2242 |
| avg_hold_time_bars | 6.7699 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
