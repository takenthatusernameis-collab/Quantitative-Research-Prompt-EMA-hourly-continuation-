# EMA Hourly Continuation — T/USDT P12_89

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.6221 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.9680 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -4.3351 |
| sortino_ratio | -1.5223 |
| max_drawdown | 0.8522 |
| cagr | -0.5196 |
| net_avg_win | 47.8334 |
| net_avg_loss | -65.7760 |
| avg_hold_time_bars | 18.1129 |
| exposure | 0.5155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
