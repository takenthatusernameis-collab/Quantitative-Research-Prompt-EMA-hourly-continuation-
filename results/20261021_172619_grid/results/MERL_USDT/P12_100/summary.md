# EMA Hourly Continuation — MERL/USDT P12_100

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.8889 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0309 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -0.8401 |
| sortino_ratio | -0.2578 |
| max_drawdown | 0.3770 |
| cagr | -0.1155 |
| net_avg_win | 91.6361 |
| net_avg_loss | -105.3750 |
| avg_hold_time_bars | 29.4639 |
| exposure | 0.6137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
