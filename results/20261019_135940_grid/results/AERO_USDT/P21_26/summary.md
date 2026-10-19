# EMA Hourly Continuation — AERO/USDT P21_26

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.1700 |
| net_win_rate | 0.3541 |
| gross_profit_factor | 0.4624 |
| gross_win_rate | 0.3943 |
| sharpe_ratio | -13.7634 |
| sortino_ratio | -6.6165 |
| max_drawdown | 0.9999 |
| cagr | -0.9708 |
| net_avg_win | 5.2915 |
| net_avg_loss | -17.0629 |
| avg_hold_time_bars | 1.7155 |
| exposure | 0.0852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
