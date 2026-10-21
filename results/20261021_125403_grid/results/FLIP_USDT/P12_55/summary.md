# EMA Hourly Continuation — FLIP/USDT P12_55

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6663 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9416 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -3.2146 |
| sortino_ratio | -1.0130 |
| max_drawdown | 0.7093 |
| cagr | -0.3815 |
| net_avg_win | 58.8038 |
| net_avg_loss | -80.4720 |
| avg_hold_time_bars | 19.2645 |
| exposure | 0.4370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
