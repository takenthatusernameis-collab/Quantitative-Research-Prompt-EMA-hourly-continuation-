# EMA Hourly Continuation — POKT/USDT P55_144

**Symbol:** POKT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.5172 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.8020 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -5.6635 |
| sortino_ratio | -1.9866 |
| max_drawdown | 0.9102 |
| cagr | -0.6128 |
| net_avg_win | 37.8815 |
| net_avg_loss | -51.8521 |
| avg_hold_time_bars | 10.2855 |
| exposure | 0.2886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
