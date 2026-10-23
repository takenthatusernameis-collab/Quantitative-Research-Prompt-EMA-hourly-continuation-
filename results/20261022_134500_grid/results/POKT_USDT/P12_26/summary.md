# EMA Hourly Continuation — POKT/USDT P12_26

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1389 |
| net_profit_factor | 0.3959 |
| net_win_rate | 0.3470 |
| gross_profit_factor | 0.8833 |
| gross_win_rate | 0.3722 |
| sharpe_ratio | -13.3199 |
| sortino_ratio | -6.9887 |
| max_drawdown | 0.9999 |
| cagr | -0.9706 |
| net_avg_win | 13.5929 |
| net_avg_loss | -18.2474 |
| avg_hold_time_bars | 3.6285 |
| exposure | 0.2281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
