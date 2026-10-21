# EMA Hourly Continuation — NMR/USDT P8_100

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.8669 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.0659 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -1.2178 |
| sortino_ratio | -0.4321 |
| max_drawdown | 0.4964 |
| cagr | -0.1839 |
| net_avg_win | 82.3890 |
| net_avg_loss | -101.4609 |
| avg_hold_time_bars | 21.2402 |
| exposure | 0.5909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
