# EMA Hourly Continuation — BDX/USDT P12_21

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.2722 |
| net_win_rate | 0.3116 |
| gross_profit_factor | 0.4751 |
| gross_win_rate | 0.3163 |
| sharpe_ratio | -5.5558 |
| sortino_ratio | -1.1761 |
| max_drawdown | 0.7534 |
| cagr | -0.4274 |
| net_avg_win | 42.0464 |
| net_avg_loss | -69.9408 |
| avg_hold_time_bars | 3.8140 |
| exposure | 0.0373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
