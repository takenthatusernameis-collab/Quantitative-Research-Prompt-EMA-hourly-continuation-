# EMA Hourly Continuation — MANTA/USDT P12_55

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.7818 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -2.1208 |
| sortino_ratio | -0.7723 |
| max_drawdown | 0.5940 |
| cagr | -0.2996 |
| net_avg_win | 66.1943 |
| net_avg_loss | -82.6002 |
| avg_hold_time_bars | 13.5000 |
| exposure | 0.3976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
