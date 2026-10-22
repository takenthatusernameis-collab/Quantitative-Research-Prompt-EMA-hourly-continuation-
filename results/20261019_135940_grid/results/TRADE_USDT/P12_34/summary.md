# EMA Hourly Continuation — TRADE/USDT P12_34

**Symbol:** TRADE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1065 |
| net_profit_factor | 0.5301 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -8.2535 |
| sortino_ratio | -3.7704 |
| max_drawdown | 0.9923 |
| cagr | -0.8491 |
| net_avg_win | 24.7390 |
| net_avg_loss | -34.4135 |
| avg_hold_time_bars | 5.2272 |
| exposure | 0.2530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
