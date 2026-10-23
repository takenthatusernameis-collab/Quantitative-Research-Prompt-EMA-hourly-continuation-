# EMA Hourly Continuation — NMR/USDT P12_89

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 821 |
| net_profit_factor | 0.6489 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -4.7438 |
| sortino_ratio | -1.9151 |
| max_drawdown | 0.9028 |
| cagr | -0.5977 |
| net_avg_win | 43.1260 |
| net_avg_loss | -58.6873 |
| avg_hold_time_bars | 13.7527 |
| exposure | 0.5132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
