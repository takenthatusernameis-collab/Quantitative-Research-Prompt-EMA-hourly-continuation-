# EMA Hourly Continuation — CFG/USDT P12_55

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7338 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -1.8903 |
| sortino_ratio | -0.5951 |
| max_drawdown | 0.5168 |
| cagr | -0.2402 |
| net_avg_win | 58.2123 |
| net_avg_loss | -74.5913 |
| avg_hold_time_bars | 22.0103 |
| exposure | 0.4872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
