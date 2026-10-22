# EMA Hourly Continuation — ICP/USDT P8_20

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1690 |
| net_profit_factor | 0.3948 |
| net_win_rate | 0.4349 |
| gross_profit_factor | 0.8396 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -12.0741 |
| sortino_ratio | -7.0212 |
| max_drawdown | 0.9999 |
| cagr | -0.9720 |
| net_avg_win | 8.8759 |
| net_avg_loss | -17.3010 |
| avg_hold_time_bars | 2.6775 |
| exposure | 0.2057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
