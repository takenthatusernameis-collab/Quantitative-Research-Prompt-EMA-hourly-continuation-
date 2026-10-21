# EMA Hourly Continuation — WOO/USDT P50_55

**Symbol:** WOO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 154 |
| net_profit_factor | 0.7125 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0313 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.3449 |
| sortino_ratio | -0.2403 |
| max_drawdown | 0.2800 |
| cagr | -0.1040 |
| net_avg_win | 76.5635 |
| net_avg_loss | -110.2812 |
| avg_hold_time_bars | 5.6753 |
| exposure | 0.0397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
