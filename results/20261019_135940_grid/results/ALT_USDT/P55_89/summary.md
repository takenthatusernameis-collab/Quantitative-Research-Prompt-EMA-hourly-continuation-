# EMA Hourly Continuation — ALT/USDT P55_89

**Symbol:** ALT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.5313 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8959 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -4.9623 |
| sortino_ratio | -1.7505 |
| max_drawdown | 0.8760 |
| cagr | -0.5628 |
| net_avg_win | 34.9222 |
| net_avg_loss | -55.7196 |
| avg_hold_time_bars | 5.5283 |
| exposure | 0.1555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
