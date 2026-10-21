# EMA Hourly Continuation — PENDLE/USDT P21_26

**Symbol:** PENDLE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.8289 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.1150 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -0.8169 |
| sortino_ratio | -0.1646 |
| max_drawdown | 0.2649 |
| cagr | -0.0735 |
| net_avg_win | 82.0940 |
| net_avg_loss | -110.8775 |
| avg_hold_time_bars | 4.7487 |
| exposure | 0.0421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
