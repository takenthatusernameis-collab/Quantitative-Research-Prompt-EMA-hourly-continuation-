# EMA Hourly Continuation — STX/USDT P12_20

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.7490 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0443 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -1.4639 |
| sortino_ratio | -0.3495 |
| max_drawdown | 0.3824 |
| cagr | -0.1481 |
| net_avg_win | 69.8775 |
| net_avg_loss | -98.8660 |
| avg_hold_time_bars | 5.0580 |
| exposure | 0.0632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
