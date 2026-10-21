# EMA Hourly Continuation — STX/USDT P12_89

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7940 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -1.4588 |
| sortino_ratio | -0.4559 |
| max_drawdown | 0.4884 |
| cagr | -0.1905 |
| net_avg_win | 66.6621 |
| net_avg_loss | -83.6031 |
| avg_hold_time_bars | 25.8601 |
| exposure | 0.5605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
