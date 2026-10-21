# EMA Hourly Continuation — ALT/USDT P55_89

**Symbol:** ALT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6728 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -2.3494 |
| sortino_ratio | -0.6549 |
| max_drawdown | 0.5366 |
| cagr | -0.2585 |
| net_avg_win | 59.0200 |
| net_avg_loss | -82.3515 |
| avg_hold_time_bars | 7.5158 |
| exposure | 0.1298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
