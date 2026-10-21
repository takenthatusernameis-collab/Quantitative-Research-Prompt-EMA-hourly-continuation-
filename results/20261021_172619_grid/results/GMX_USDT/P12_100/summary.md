# EMA Hourly Continuation — GMX/USDT P12_100

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.7546 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9470 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -2.2545 |
| sortino_ratio | -0.7438 |
| max_drawdown | 0.6125 |
| cagr | -0.2899 |
| net_avg_win | 68.7491 |
| net_avg_loss | -84.2469 |
| avg_hold_time_bars | 22.4991 |
| exposure | 0.5492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
