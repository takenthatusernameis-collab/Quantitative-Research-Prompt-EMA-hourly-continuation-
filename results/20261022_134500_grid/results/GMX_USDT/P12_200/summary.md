# EMA Hourly Continuation — GMX/USDT P12_200

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7154 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9577 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -2.4255 |
| sortino_ratio | -0.7339 |
| max_drawdown | 0.6119 |
| cagr | -0.2905 |
| net_avg_win | 66.3025 |
| net_avg_loss | -85.2819 |
| avg_hold_time_bars | 34.0985 |
| exposure | 0.7083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
