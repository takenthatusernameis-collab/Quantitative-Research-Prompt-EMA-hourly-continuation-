# EMA Hourly Continuation — ERG/USDT P12_50

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.3596 |
| net_win_rate | 0.3844 |
| gross_profit_factor | 0.6362 |
| gross_win_rate | 0.3924 |
| sharpe_ratio | -10.4683 |
| sortino_ratio | -4.9719 |
| max_drawdown | 0.9981 |
| cagr | -0.9170 |
| net_avg_win | 12.9138 |
| net_avg_loss | -22.4249 |
| avg_hold_time_bars | 6.3437 |
| exposure | 0.3255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
