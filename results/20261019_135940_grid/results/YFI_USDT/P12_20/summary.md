# EMA Hourly Continuation — YFI/USDT P12_20

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1577 |
| net_profit_factor | 0.1729 |
| net_win_rate | 0.3551 |
| gross_profit_factor | 0.7657 |
| gross_win_rate | 0.4318 |
| sharpe_ratio | -16.8943 |
| sortino_ratio | -9.7701 |
| max_drawdown | 1.0000 |
| cagr | -0.9941 |
| net_avg_win | 3.7325 |
| net_avg_loss | -11.8881 |
| avg_hold_time_bars | 2.5688 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
