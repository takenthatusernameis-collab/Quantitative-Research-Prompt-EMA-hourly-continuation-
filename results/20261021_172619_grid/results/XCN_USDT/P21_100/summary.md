# EMA Hourly Continuation — XCN/USDT P21_100

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.7270 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9139 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -2.2599 |
| sortino_ratio | -0.6977 |
| max_drawdown | 0.5586 |
| cagr | -0.2752 |
| net_avg_win | 65.9269 |
| net_avg_loss | -82.5690 |
| avg_hold_time_bars | 17.5511 |
| exposure | 0.3750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
