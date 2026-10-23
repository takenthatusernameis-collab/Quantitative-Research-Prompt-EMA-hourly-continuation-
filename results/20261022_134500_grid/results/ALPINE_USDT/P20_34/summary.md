# EMA Hourly Continuation — ALPINE/USDT P20_34

**Symbol:** ALPINE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.3410 |
| net_win_rate | 0.3757 |
| gross_profit_factor | 0.7009 |
| gross_win_rate | 0.4175 |
| sharpe_ratio | -11.1389 |
| sortino_ratio | -5.0937 |
| max_drawdown | 0.9984 |
| cagr | -0.9235 |
| net_avg_win | 13.3522 |
| net_avg_loss | -23.5638 |
| avg_hold_time_bars | 4.3107 |
| exposure | 0.2018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
