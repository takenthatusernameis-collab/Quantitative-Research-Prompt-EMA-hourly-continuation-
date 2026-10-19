# EMA Hourly Continuation — GRT/USDT P26_144

**Symbol:** GRT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6332 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9767 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -3.1316 |
| sortino_ratio | -0.9640 |
| max_drawdown | 0.7049 |
| cagr | -0.3741 |
| net_avg_win | 50.7186 |
| net_avg_loss | -75.3110 |
| avg_hold_time_bars | 21.6448 |
| exposure | 0.4770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
