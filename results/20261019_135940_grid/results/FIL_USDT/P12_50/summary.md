# EMA Hourly Continuation — FIL/USDT P12_50

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.4854 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -6.6866 |
| sortino_ratio | -3.0486 |
| max_drawdown | 0.9771 |
| cagr | -0.7755 |
| net_avg_win | 18.8368 |
| net_avg_loss | -33.3506 |
| avg_hold_time_bars | 7.5142 |
| exposure | 0.3614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
