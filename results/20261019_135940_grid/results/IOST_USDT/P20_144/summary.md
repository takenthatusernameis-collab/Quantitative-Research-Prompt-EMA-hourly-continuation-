# EMA Hourly Continuation — IOST/USDT P20_144

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7333 |
| net_win_rate | 0.5171 |
| gross_profit_factor | 1.1069 |
| gross_win_rate | 0.5272 |
| sharpe_ratio | -2.1843 |
| sortino_ratio | -0.6891 |
| max_drawdown | 0.6029 |
| cagr | -0.2806 |
| net_avg_win | 60.1821 |
| net_avg_loss | -87.8869 |
| avg_hold_time_bars | 23.6660 |
| exposure | 0.5346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
