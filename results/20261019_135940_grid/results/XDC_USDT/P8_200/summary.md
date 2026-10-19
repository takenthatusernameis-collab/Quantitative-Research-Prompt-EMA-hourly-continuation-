# EMA Hourly Continuation — XDC/USDT P8_200

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.5288 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.9104 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -4.9791 |
| sortino_ratio | -1.6465 |
| max_drawdown | 0.8820 |
| cagr | -0.5692 |
| net_avg_win | 37.5172 |
| net_avg_loss | -60.3892 |
| avg_hold_time_bars | 26.7622 |
| exposure | 0.6958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
