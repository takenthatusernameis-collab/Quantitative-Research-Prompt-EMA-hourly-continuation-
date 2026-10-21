# EMA Hourly Continuation — ETC/USDT P21_55

**Symbol:** ETC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -3.2893 |
| sortino_ratio | -1.0541 |
| max_drawdown | 0.7147 |
| cagr | -0.3822 |
| net_avg_win | 48.5096 |
| net_avg_loss | -72.9814 |
| avg_hold_time_bars | 8.2265 |
| exposure | 0.1866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
