# EMA Hourly Continuation — HNT/USDT P20_89

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 770 |
| net_profit_factor | 0.6066 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -4.4860 |
| sortino_ratio | -1.7595 |
| max_drawdown | 0.8865 |
| cagr | -0.5661 |
| net_avg_win | 38.0916 |
| net_avg_loss | -53.7202 |
| avg_hold_time_bars | 10.8987 |
| exposure | 0.3815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
