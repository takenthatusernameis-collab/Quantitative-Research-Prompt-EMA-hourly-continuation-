# EMA Hourly Continuation — TRX/USDT P12_34

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1125 |
| net_profit_factor | 0.1861 |
| net_win_rate | 0.3271 |
| gross_profit_factor | 0.9318 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -16.1893 |
| sortino_ratio | -8.2198 |
| max_drawdown | 1.0000 |
| cagr | -0.9895 |
| net_avg_win | 6.2140 |
| net_avg_loss | -16.2307 |
| avg_hold_time_bars | 4.3102 |
| exposure | 0.2204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
