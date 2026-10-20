# EMA Hourly Continuation — ARKM/USDT P34_89

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.8885 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -4.5816 |
| sortino_ratio | -1.7306 |
| max_drawdown | 0.8740 |
| cagr | -0.5596 |
| net_avg_win | 35.3011 |
| net_avg_loss | -53.6131 |
| avg_hold_time_bars | 6.7497 |
| exposure | 0.2194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
