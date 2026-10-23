# EMA Hourly Continuation — WOO/USDT P8_50

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.6793 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 1.0715 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -4.9183 |
| sortino_ratio | -2.2849 |
| max_drawdown | 0.9419 |
| cagr | -0.6637 |
| net_avg_win | 37.5867 |
| net_avg_loss | -51.7943 |
| avg_hold_time_bars | 9.3303 |
| exposure | 0.4623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
