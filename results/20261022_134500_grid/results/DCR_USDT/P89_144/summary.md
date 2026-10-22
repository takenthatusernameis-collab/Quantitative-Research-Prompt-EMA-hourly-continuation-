# EMA Hourly Continuation — DCR/USDT P89_144

**Symbol:** DCR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.4333 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.8083 |
| gross_win_rate | 0.4434 |
| sharpe_ratio | -5.6108 |
| sortino_ratio | -1.8103 |
| max_drawdown | 0.8902 |
| cagr | -0.5822 |
| net_avg_win | 30.4944 |
| net_avg_loss | -52.6642 |
| avg_hold_time_bars | 5.7869 |
| exposure | 0.1364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
