# EMA Hourly Continuation — APT/USDT P55_89

**Symbol:** APT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7261 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9898 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.6177 |
| sortino_ratio | -0.3951 |
| max_drawdown | 0.4079 |
| cagr | -0.1652 |
| net_avg_win | 66.6382 |
| net_avg_loss | -92.4173 |
| avg_hold_time_bars | 6.0173 |
| exposure | 0.0790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
