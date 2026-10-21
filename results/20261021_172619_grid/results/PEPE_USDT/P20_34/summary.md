# EMA Hourly Continuation — PEPE/USDT P20_34

**Symbol:** PEPE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.6057 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.7941 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -2.5585 |
| sortino_ratio | -0.5797 |
| max_drawdown | 0.4922 |
| cagr | -0.2337 |
| net_avg_win | 66.8780 |
| net_avg_loss | -87.0838 |
| avg_hold_time_bars | 5.4370 |
| exposure | 0.0628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
