# EMA Hourly Continuation — DBR/USDT P20_26

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.6004 |
| net_win_rate | 0.5195 |
| gross_profit_factor | 1.1522 |
| gross_win_rate | 0.5325 |
| sharpe_ratio | -2.5891 |
| sortino_ratio | -0.6288 |
| max_drawdown | 0.4826 |
| cagr | -0.2538 |
| net_avg_win | 55.6268 |
| net_avg_loss | -100.1642 |
| avg_hold_time_bars | 6.8745 |
| exposure | 0.0903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
