# EMA Hourly Continuation — BDX/USDT P8_26

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1876 |
| net_profit_factor | 0.2354 |
| net_win_rate | 0.2303 |
| gross_profit_factor | 0.6389 |
| gross_win_rate | 0.2958 |
| sharpe_ratio | -25.4909 |
| sortino_ratio | -17.0591 |
| max_drawdown | 1.0000 |
| cagr | -0.9999 |
| net_avg_win | 7.1257 |
| net_avg_loss | -9.0570 |
| avg_hold_time_bars | 2.5506 |
| exposure | 0.2175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
