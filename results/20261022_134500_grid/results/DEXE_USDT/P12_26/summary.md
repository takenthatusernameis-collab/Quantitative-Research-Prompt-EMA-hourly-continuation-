# EMA Hourly Continuation — DEXE/USDT P12_26

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1439 |
| net_profit_factor | 0.2523 |
| net_win_rate | 0.3836 |
| gross_profit_factor | 0.5801 |
| gross_win_rate | 0.4135 |
| sharpe_ratio | -12.8900 |
| sortino_ratio | -6.9629 |
| max_drawdown | 0.9999 |
| cagr | -0.9706 |
| net_avg_win | 6.1122 |
| net_avg_loss | -15.0761 |
| avg_hold_time_bars | 4.2842 |
| exposure | 0.2802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
