# EMA Hourly Continuation — LISTA/USDT P144_200

**Symbol:** LISTA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.6292 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8467 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -2.1365 |
| sortino_ratio | -0.4837 |
| max_drawdown | 0.4067 |
| cagr | -0.2004 |
| net_avg_win | 62.7355 |
| net_avg_loss | -87.7438 |
| avg_hold_time_bars | 7.4170 |
| exposure | 0.0852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
