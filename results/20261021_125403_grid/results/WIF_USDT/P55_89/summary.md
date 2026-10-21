# EMA Hourly Continuation — WIF/USDT P55_89

**Symbol:** WIF/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.8677 |
| net_win_rate | 0.5235 |
| gross_profit_factor | 1.0838 |
| gross_win_rate | 0.5235 |
| sharpe_ratio | -0.6881 |
| sortino_ratio | -0.1651 |
| max_drawdown | 0.2391 |
| cagr | -0.0750 |
| net_avg_win | 80.4173 |
| net_avg_loss | -101.8069 |
| avg_hold_time_bars | 7.1625 |
| exposure | 0.0902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
