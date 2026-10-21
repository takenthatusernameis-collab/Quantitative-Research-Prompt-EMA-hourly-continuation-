# EMA Hourly Continuation — JTO/USDT P12_55

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.8109 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9889 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.8036 |
| sortino_ratio | -0.6555 |
| max_drawdown | 0.5782 |
| cagr | -0.2624 |
| net_avg_win | 71.8393 |
| net_avg_loss | -86.4246 |
| avg_hold_time_bars | 12.9133 |
| exposure | 0.3792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
