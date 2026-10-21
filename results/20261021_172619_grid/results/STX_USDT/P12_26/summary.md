# EMA Hourly Continuation — STX/USDT P12_26

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.6335 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8647 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -3.0193 |
| sortino_ratio | -0.9162 |
| max_drawdown | 0.6632 |
| cagr | -0.3432 |
| net_avg_win | 53.2991 |
| net_avg_loss | -74.0077 |
| avg_hold_time_bars | 5.6336 |
| exposure | 0.1155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
