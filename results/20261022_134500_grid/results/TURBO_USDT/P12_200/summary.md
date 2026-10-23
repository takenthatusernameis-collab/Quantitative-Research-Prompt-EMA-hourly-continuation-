# EMA Hourly Continuation — TURBO/USDT P12_200

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7047 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9504 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -2.6449 |
| sortino_ratio | -0.8012 |
| max_drawdown | 0.5740 |
| cagr | -0.3144 |
| net_avg_win | 71.2201 |
| net_avg_loss | -91.1013 |
| avg_hold_time_bars | 32.9249 |
| exposure | 0.6933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
